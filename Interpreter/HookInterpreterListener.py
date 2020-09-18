# Generated from .\Interpreter\HookInterpreter.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HookInterpreterParser import HookInterpreterParser
else:
    from HookInterpreterParser import HookInterpreterParser

# This class defines a complete listener for a parse tree produced by HookInterpreterParser.
class HookInterpreterListener(ParseTreeListener):

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


    # Enter a parse tree produced by HookInterpreterParser#includeSentence.
    def enterIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#includeSentence.
    def exitIncludeSentence(self, ctx:HookInterpreterParser.IncludeSentenceContext):
        pass


    # Enter a parse tree produced by HookInterpreterParser#variableDeclare.
    def enterVariableDeclare(self, ctx:HookInterpreterParser.VariableDeclareContext):
        pass

    # Exit a parse tree produced by HookInterpreterParser#variableDeclare.
    def exitVariableDeclare(self, ctx:HookInterpreterParser.VariableDeclareContext):
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



del HookInterpreterParser