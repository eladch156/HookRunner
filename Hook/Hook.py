from App.Logger import Logger
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from Hook.Step import StepBase,StepInclude,StepDeclVar,StepType
from Interpreter.HookInterpreterLexer import HookInterpreterLexer
from Interpreter.HookInterpreterListener import HookInterpreterListener
from Interpreter.HookInterpreterParser import HookInterpreterParser
import logging
from typing import List
StepList = List[StepBase]

class MainInterpreterListener(HookInterpreterListener):
    def __init__(self):
        HookInterpreterListener.__init__(self)
        self._logger = Logger("Interpreter","Listener")
        self._steps = []
    
    def getSteps(self):
        return self._steps

    # Enter a parse tree produced by HookInterpreterParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:HookInterpreterParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:HookInterpreterParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#sentenceEnding.
    def enterSentenceEnding(self, ctx:HookInterpreterParser.SentenceEndingContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#sentenceEnding.
    def exitSentenceEnding(self, ctx:HookInterpreterParser.SentenceEndingContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#variableDeclare.
    def enterVariableDeclare(self, ctx:HookInterpreterParser.VariableDeclareContext):
        self._steps.append(StepDeclVar(ctx.Identifier(),ctx.FreeText()))
        self._logger.log(logging.INFO,"Found step: {}",self._steps[-1].what())

    # Exit a parse tree produced by HookInterpreterParser#variableDeclare.
    def exitVariableDeclare(self, ctx:HookInterpreterParser.VariableDeclareContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#includeSentence.
    def enterIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        self._steps.append(StepInclude(ctx.Identifier(0),ctx.Identifier(1)))
        self._logger.log(logging.INFO,"Found step: {}",self._steps[-1].what())


    # Exit a parse tree produced by HookInterpreterParser#includeSentence.
    def exitIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#argument.
    def enterArgument(self, ctx:HookInterpreterParser.ArgumentContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#argument.
    def exitArgument(self, ctx:HookInterpreterParser.ArgumentContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#arguments.
    def enterArguments(self, ctx:HookInterpreterParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#arguments.
    def exitArguments(self, ctx:HookInterpreterParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#functionCall.
    def enterFunctionCall(self, ctx:HookInterpreterParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#functionCall.
    def exitFunctionCall(self, ctx:HookInterpreterParser.FunctionCallContext):
        pass


def getStepDescription(name):
    switch = {
        StepType.INCLUDE: "Include library step.",
        StepType.VAR: "Variable declare step."
    }
    return switch[name] if name in switch else ""

def execute(steps: StepList):
    _logger = Logger("Hook","Execute","Main")
    for _step in steps:
        _logger.log(logging.INFO,"Found step: {}",_step.what())
        _step.run()

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

def runHook(hookPath):
    _input = FileStream(hookPath)
    _lexer = HookInterpreterLexer(_input)
    _stream = CommonTokenStream(_lexer)
    _parser = HookInterpreterParser(_stream)
    _tree = _parser.primaryExpression()
    traverse(_tree,_parser.ruleNames)
    _listener = MainInterpreterListener()
    _walker = ParseTreeWalker()
    _walker.walk(_listener, _tree)
    execute(_listener.getSteps())



