from App.Logger import Logger
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from Hook.Step import StepBase, StepInclude, StepDeclVar, StepType
from Hook.Step import StepRunCommand, StepsData, StepAssignment, AssignmentType
from Interpreter.HookInterpreterLexer import HookInterpreterLexer
from Interpreter.HookInterpreterListener import HookInterpreterListener
from Interpreter.HookInterpreterParser import HookInterpreterParser
from antlr4.error.ErrorListener import ErrorListener
from uuid import uuid4
from typing import List
from io import StringIO
from Utils.Exceptions import AntlrExcption


def _read_arguments(arg_list):
    _args_text_list = []
    for arg in arg_list:
        _args_text_list.append(arg.getText())
    return _args_text_list


class MainInterpreterListener(HookInterpreterListener):
    def __init__(self):
        HookInterpreterListener.__init__(self)
        self.__logger = Logger("Interpreter", "Listener")
        self.__steps = []
        self.__out = StringIO()
        self.__err = StringIO()

    def get_steps(self):
        return self.__steps

    def enterPrimaryExpression(self, ctx):
        pass

    def exitPrimaryExpression(self, ctx):
        pass

    def enterIncludeSentence(self, ctx):
        _desc = (StepType.INCLUDE, _get_step_description(StepType.INCLUDE))
        _lib = ctx.Identifier(0).getText()
        _func = ctx.Identifier(1).getText()
        self.__steps.append(StepInclude(_lib, _func))
        self.__logger.log("Info",
                          "Found step: "
                          "{}.", str(_desc))

    def exitIncludeSentence(self, ctx):
        pass

    def enterValue(self, ctx):
        pass

    def exitValue(self, ctx):
        pass

    def enterValues(self, ctx):
        pass

    def exitValues(self, ctx):
        pass

    def enterFunctionCall(self, ctx):
        _desc = (StepType.EXECUTE, _get_step_description(StepType.EXECUTE))
        args = [] if ctx.values() is None else _read_arguments(ctx.values())
        _ctx_uuid = ctx.uuid if hasattr(ctx, "uuid") else None
        self.__steps.append(StepRunCommand(*args,
                                           name=ctx.Identifier(0).getText(),
                                           uuid=_ctx_uuid))
        self.__logger.log("Info", "Found step: {}", str(_desc))

    def exitFunctionCall(self, ctx):
        pass

    def enterAssigmentWithOutDecl(self, ctx):
        _name = ctx.value(0).getText()
        if ctx.value(1):
            _value = ctx.value(1).getText()
        else:
            _value = None
        _desc = (StepType.ASSIGNMENT, _get_step_description(
                                        StepType.ASSIGNMENT))
        if not ctx.value(0).Identifier():
            # TODO:Error
            pass
        if hasattr(ctx, '_decl'):
            if not ctx.AssigmentOpreator().getText() != "=":
                # TODO:Error
                pass
            if ctx.functionCall():
                _func_uuid = uuid4()
                ctx.functionCall().uuid = _func_uuid
                self.__steps.append(StepDeclVar(_name, "", _func_uuid))
            elif _value:
                _value_as_id = ctx.value(1).Identifier()
                _value_as_num = ctx.value(1).Digits()
                if _value_as_id or _value_as_num:
                    self.__steps.append(StepDeclVar(_name, _value))
                else:
                    self.__steps.append(StepDeclVar(_name, _value[1:-1]))
        if ctx.functionCall():
            _func_uuid = uuid4()
            ctx.functionCall().uuid = _func_uuid
            self.__steps.append(StepAssignment(
                                _name,
                                _func_uuid,
                                AssignmentType.FUNCTION,
                                ctx.AssigmentOpreator().getText()))
        elif _value:
            _op = ctx.AssigmentOpreator().getText()
            _value_as_id = ctx.value(1).Identifier()
            if _value_as_id:
                self.__steps.append(StepAssignment(_name,
                                                   _value,
                                                   AssignmentType.VARIBLE,
                                                   _op))
            else:
                self.__steps.append(StepAssignment(_name,
                                                   _value,
                                                   AssignmentType.VALUE,
                                                   _op))
        self.__logger.log("Info", "Found step: {}.", str(_desc))

    def exitAssigmentWithOutDecl(self, ctx):
        pass

    def enterAssigmentWithDecl(self, ctx):
        ctx.assigmentWithOutDecl()._decl = True

    def exitAssigmentWithDecl(self, ctx):
        pass

    def enterMultiAssingment(self, ctx):
        pass

    def exitMultiAssingment(self, ctx):
        pass


def _get_step_description(name):
    switch = {
        StepType.INCLUDE: "Include library step.",
        StepType.VAR: "Variable declare step.",
        StepType.EXECUTE: "Run a library command.",
        StepType.ASSIGNMENT: "Assign value to variable => variable,"
                             "function or value."
    }
    return switch[name] if name in switch else ""


def _execute(steps):
    _logger = Logger("Hook", "Execute", "Main")
    _data = StepsData()
    for _step in steps:
        _step.set_step_data(_data)
        try:
            _logger.log("Info", "Start: {}", _step.what())
            if not _step.run():
                _logger.log("Info", "End(Failure): {}", _step.what())
                break
            _logger.log("Info", "End(Success): {}", _step.what())
        except Exception as ex:
            _logger.log("Info", "End(Error): {}", str(ex))
            break
    _logger.log("Info", "Stack Data: {}", str(_data))


def _traverse(tree, rule_names, indent=0):
    _logger = Logger("Hook", "Execute", "TreverseScript")
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        _logger.log("Info", "{0}TOKEN='{1}'".format("  " * indent,
                                                    tree.getText()))
    else:
        _logger.log("Info",
                    "{0}{1}".format("  " * indent,
                                    rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            _traverse(child, rule_names, indent + 1)


class HookRunnerErrorListener(ErrorListener):
    def __init__(self):
        super(HookRunnerErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise AntlrExcption("SyntaxError",
                            "Symbol : {} , Line {}:{} "
                            "=> {}".format(offendingSymbol, line, column, msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex,
                        stopIndex, exact, ambigAlts, configs):
        raise AntlrExcption("ReporterAmbiguity", "")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex,
                                    stopIndex, conflictingAlts, configs):
        raise AntlrExcption("ReporterAttemptingFullContext",
                            "Deterministic Finite Automata : {},"
                            " Start : {},"
                            " End: {},"
                            " Conflicting : {},"
                            " Configs : {}".format(
                                dfa,
                                startIndex,
                                stopIndex,
                                conflictingAlts,
                                configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex,
                                 prediction, configs):
        raise AntlrExcption("ReporterContextSensitivity", "")


def run_hook(hook_path):
    _logger = Logger("Hook", "AST")
    _input = FileStream(hook_path)
    _lexer = HookInterpreterLexer(_input)
    _stream = CommonTokenStream(_lexer)
    _parser = HookInterpreterParser(_stream)
    _parser.addErrorListener(DiagnosticErrorListener())
    _parser.addErrorListener(HookRunnerErrorListener())
    _tree = _parser.primaryExpression()
    _traverse(_tree, _parser.ruleNames)
    _listener = MainInterpreterListener()
    _walker = ParseTreeWalker()
    _walker.walk(_listener, _tree)
    _execute(_listener.get_steps())
