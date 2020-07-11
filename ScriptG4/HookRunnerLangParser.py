# Generated from .\HookRunnerLang.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\n\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class HookRunnerLangParser ( Parser ):

    grammarFileName = "HookRunnerLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IF'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Then'", "'End'", "'Import'" ]

    symbolicNames = [ "<INVALID>", "IF", "WS", "NAME", "CONDITION_OPERATOR", 
                      "THEN", "END", "IMPORT", "Sentence", "Number", "String", 
                      "Import", "Value", "Variable", "Condition", "Args", 
                      "Command" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    IF=1
    WS=2
    NAME=3
    CONDITION_OPERATOR=4
    THEN=5
    END=6
    IMPORT=7
    Sentence=8
    Number=9
    String=10
    Import=11
    Value=12
    Variable=13
    Condition=14
    Args=15
    Command=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Sentence(self):
            return self.getToken(HookRunnerLangParser.Sentence, 0)

        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = HookRunnerLangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HookRunnerLangParser.Sentence)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





