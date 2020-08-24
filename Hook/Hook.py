from App.Logger import Logger
from antlr4 import *
from Hook.Step import StepBase,StepInclude,StepDeclVar,StepType
from Interpreter.HookInterpreterParserLexer import HookInterpreterParserLexer
from Interpreter.HookInterpreterParserParser import HookInterpreterParserParser
from Interpreter.HookInterpreterParserListener import HookInterpreterParserListener
import logging
from typing import List
StepList = List[StepBase]

class BaseInterpreterListener(HookInterpreterParserListener):
    def BaseInterpreterListener(self):
        HookInterpreterParserListener.__init__()
        self._logger = Logger("Interpreter","Listener")
        self._steps = []

    def getSteps(self):
        return self._steps

    # Enter a parse tree produced by HookInterpreterParserParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:HookInterpreterParserParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:HookInterpreterParserParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by HookInterpreterParserParser#sentenceEnding.
    def enterSentenceEnding(self, ctx:HookInterpreterParserParser.SentenceEndingContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#sentenceEnding.
    def exitSentenceEnding(self, ctx:HookInterpreterParserParser.SentenceEndingContext):
        pass


    # Enter a parse tree produced by HookInterpreterParserParser#variableDeclare.
    def enterVariableDeclare(self, ctx:HookInterpreterParserParser.VariableDeclareContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#variableDeclare.
    def exitVariableDeclare(self, ctx:HookInterpreterParserParser.VariableDeclareContext):
        self._steps.append(StepDeclVar(ctx.Identifier(),ctx.NotNewLine()))


    # Enter a parse tree produced by HookInterpreterParserParser#includeSentence.
    def enterIncludeSentence(self, ctx:HookInterpreterParserParser.IncludeSentenceContext):
        self._steps.append(StepInclude(ctx.NotNewLine(0),ctx.NotNewLine(1)))

    # Exit a parse tree produced by HookInterpreterParserParser#includeSentence.
    def exitIncludeSentence(self, ctx:HookInterpreterParserParser.IncludeSentenceContext):
        pass


    # Enter a parse tree produced by HookInterpreterParserParser#argument.
    def enterArgument(self, ctx:HookInterpreterParserParser.ArgumentContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#argument.
    def exitArgument(self, ctx:HookInterpreterParserParser.ArgumentContext):
        pass


    # Enter a parse tree produced by HookInterpreterParserParser#arguments.
    def enterArguments(self, ctx:HookInterpreterParserParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#arguments.
    def exitArguments(self, ctx:HookInterpreterParserParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by HookInterpreterParserParser#functionCall.
    def enterFunctionCall(self, ctx:HookInterpreterParserParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by HookInterpreterParserParser#functionCall.
    def exitFunctionCall(self, ctx:HookInterpreterParserParser.FunctionCallContext):
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
        

def runHook(hookPath):
    _input = FileStream(hookPath)
    _lexer = HookInterpreterParserLexer(_input)
    _stream = CommonTokenStream(_lexer)
    _parser = HookInterpreterParserParser(_stream)
    _tree = _parser.primaryExpression()
    _listener = BaseInterpreterListener()
    _walker = ParseTreeWalker()
    _walker.walk(_listener, _tree)
    execute(_listener.getSteps())



