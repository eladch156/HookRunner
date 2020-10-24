from App.Logger import Logger
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from Hook.Step import StepBase,StepInclude,StepDeclVar,StepType,StepRunCommand,StepsData,StepAssignment,AssignmentType
from Interpreter.HookInterpreterLexer import HookInterpreterLexer
from Interpreter.HookInterpreterListener import HookInterpreterListener
from Interpreter.HookInterpreterParser import HookInterpreterParser
from antlr4.error.ErrorListener import ErrorListener
from uuid import uuid4
import logging
from typing import List
from io import StringIO
from Utils.Exceptions import AntlrExcption
StepList = List[StepBase]

def readArguments(argList):
    _argsTextList = []
    for arg in argList:
        _argsTextList.append(arg.getText())
    return _argsTextList

class MainInterpreterListener(HookInterpreterListener):
    def __init__(self):
        HookInterpreterListener.__init__(self)
        self._logger = Logger("Interpreter","Listener")
        self._steps = []
        self._out = StringIO()
        self._err = StringIO()
    
    def getSteps(self):
        return self._steps

    # Enter a parse tree produced by HookInterpreterParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:HookInterpreterParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:HookInterpreterParser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by HookInterpreterParser#includeSentence.
    def enterIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        self._steps.append(StepInclude(ctx.Identifier(0).getText(),ctx.Identifier(1).getText()))
        self._logger.log(logging.INFO,"Found step: {}",self._steps[-1].what())

    # Exit a parse tree produced by HookInterpreterParser#includeSentence.
    def exitIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#value.
    def enterValue(self, ctx:HookInterpreterParser.ValueContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#value.
    def exitValue(self, ctx:HookInterpreterParser.ValueContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#values.
    def enterValues(self, ctx:HookInterpreterParser.ValuesContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#values.
    def exitValues(self, ctx:HookInterpreterParser.ValuesContext):
        pass

    # Enter a parse tree produced by HookInterpreterParser#functionCall.
    def enterFunctionCall(self, ctx:HookInterpreterParser.FunctionCallContext):
        args = [] if ctx.values() is None else readArguments(ctx.values())
        self._steps.append(StepRunCommand(*args,name=ctx.Identifier(0).getText(),oPipe=self._out,ePipe=self._err,uuid=ctx.uuid if hasattr(ctx, "uuid") else None))
        self._logger.log(logging.INFO,"Found step: {}",self._steps[-1].what())

    # Exit a parse tree produced by HookInterpreterParser#functionCall.
    def exitFunctionCall(self, ctx:HookInterpreterParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#assigmentWithOutDecl.
    def enterAssigmentWithOutDecl(self, ctx:HookInterpreterParser.AssigmentWithOutDeclContext):
        if not ctx.value(0).Identifier():
            #TODO:Error 
            pass
        if hasattr(ctx, '_decl'):
            if not ctx.AssigmentOpreator().getText() != "=":
                #TODO:Error
                pass
            self._steps.append(StepDeclVar(ctx.value(0).getText(),ctx.value(1).getText()[1:-1]))
            self._logger.log(logging.INFO,"Found step: {}",self._steps[-1].what())
        if ctx.functionCall():
            ctx.functionCall().uuid = uuid4()
            self._steps.append(StepAssignment(ctx.value(0).getText(),ctx.functionCall().uuid,AssignmentType.FUNCTION,ctx.AssigmentOpreator().getText()))
            self._logger.log(logging.INFO,"Found step: {},{}",self._steps[-1].what(),AssignmentType.FUNCTION)
        elif ctx.value(1):
            if ctx.value(1).Identifier():
                self._steps.append(StepAssignment(ctx.value(0).getText(),ctx.value(1).getText(),AssignmentType.VARIBLE,ctx.AssigmentOpreator().getText()))
                self._logger.log(logging.INFO,"Found step: {},{}",self._steps[-1].what(),AssignmentType.VARIBLE)
            else:
                self._steps.append(StepAssignment(ctx.value(0).getText(),ctx.value(1).getText(),AssignmentType.VALUE,ctx.AssigmentOpreator().getText()))
                self._logger.log(logging.INFO,"Found step: {},{}",self._steps[-1].what(),AssignmentType.VALUE)

    # Exit a parse tree produced by HookInterpreterParser#assigmentWithOutDecl.
    def exitAssigmentWithOutDecl(self, ctx:HookInterpreterParser.AssigmentWithOutDeclContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#assigmentWithDecl.
    def enterAssigmentWithDecl(self, ctx:HookInterpreterParser.AssigmentWithDeclContext):
        ctx.assigmentWithOutDecl()._decl = True

    # Exit a parse tree produced by HookInterpreterParser#assigmentWithDecl.
    def exitAssigmentWithDecl(self, ctx:HookInterpreterParser.AssigmentWithDeclContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#multiAssingment.
    def enterMultiAssingment(self, ctx:HookInterpreterParser.MultiAssingmentContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#multiAssingment.
    def exitMultiAssingment(self, ctx:HookInterpreterParser.MultiAssingmentContext):
        pass

#TODO: Make it work....
def getStepDescription(name):
    switch = {
        StepType.INCLUDE: "Include library step.",
        StepType.VAR: "Variable declare step."
    }
    return switch[name] if name in switch else ""

def execute(steps: StepList):
    _logger = Logger("Hook","Execute","Main")
    _data = StepsData()
    for _step in steps:
        _step.setStepsData(_data)
        _logger.log(logging.INFO,"Found step: {}",_step.what())
        _step.run()
    _logger.log(logging.INFO, str(_data))

def traverse(tree, rule_names, indent = 0):
    _logger = Logger("Hook","Execute","TreverseScript")
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        _logger.log(logging.INFO,"{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        _logger.log(logging.INFO,"{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)


class HookRunnerErrorListener(ErrorListener):
    def __init__(self):
        super(HookRunnerErrorListener, self).__init__()
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise AntlrExcption("SyntaxError","Symbol : {} , Line {}:{} => {}".format(offendingSymbol,line,column,msg))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise AntlrExcption("ReporterAmbiguity","")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise AntlrExcption("ReporterAttemptingFullContext","Deterministic Finite Automata : {}, Start : {}, End: {}, Conflicting : {}, Configs : {}".format(dfa,startIndex,stopIndex,conflictingAlts,configs))

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise AntlrExcption("ReporterContextSensitivity","")

def runHook(hookPath):
    _logger = Logger("Hook","AST")
    _input = FileStream(hookPath)
    _lexer = HookInterpreterLexer(_input)
    _stream = CommonTokenStream(_lexer)
    _parser = HookInterpreterParser(_stream)
    _parser.addErrorListener(DiagnosticErrorListener())
    _parser.addErrorListener(HookRunnerErrorListener())
    _tree = _parser.primaryExpression()
    traverse(_tree,_parser.ruleNames)
    _listener = MainInterpreterListener()
    _walker = ParseTreeWalker()
    _walker.walk(_listener, _tree)
    execute(_listener.getSteps())




