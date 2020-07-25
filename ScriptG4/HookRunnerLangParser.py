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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\5\3\31\n\3\3\3\3")
        buf.write("\3\6\3\35\n\3\r\3\16\3\36\3\4\3\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\61\n\b\3\b\3")
        buf.write("\b\3\b\5\b\66\n\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t")
        buf.write("@\n\t\f\t\16\tC\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\nR\n\n\3\n\2\2\13\2\4\6\b\n\f\16")
        buf.write("\20\22\2\3\3\2\22\23\2P\2\24\3\2\2\2\4\34\3\2\2\2\6 \3")
        buf.write("\2\2\2\b\"\3\2\2\2\n$\3\2\2\2\f\'\3\2\2\2\16,\3\2\2\2")
        buf.write("\20A\3\2\2\2\22Q\3\2\2\2\24\25\5\4\3\2\25\3\3\2\2\2\26")
        buf.write("\31\5\16\b\2\27\31\5\22\n\2\30\26\3\2\2\2\30\27\3\2\2")
        buf.write("\2\31\32\3\2\2\2\32\33\7\3\2\2\33\35\3\2\2\2\34\30\3\2")
        buf.write("\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\5\3")
        buf.write("\2\2\2 !\7\f\2\2!\7\3\2\2\2\"#\t\2\2\2#\t\3\2\2\2$%\7")
        buf.write("\20\2\2%&\5\6\4\2&\13\3\2\2\2\'(\7\21\2\2()\5\6\4\2)*")
        buf.write("\7\24\2\2*+\5\b\5\2+\r\3\2\2\2,-\7\n\2\2-\60\7\4\2\2.")
        buf.write("\61\5\f\7\2/\61\5\b\5\2\60.\3\2\2\2\60/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\65\7\r\2\2\63\66\5\f\7\2\64\66\5\b\5\2\65")
        buf.write("\63\3\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2\678\7\5\2\289")
        buf.write("\7\16\2\29:\5\4\3\2:;\7\17\2\2;\17\3\2\2\2<=\5\6\4\2=")
        buf.write(">\7\6\2\2>@\3\2\2\2?<\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3")
        buf.write("\2\2\2BD\3\2\2\2CA\3\2\2\2DE\5\6\4\2E\21\3\2\2\2FG\5\6")
        buf.write("\4\2GH\7\7\2\2HI\5\6\4\2IJ\7\b\2\2JK\5\20\t\2KL\7\t\2")
        buf.write("\2LR\3\2\2\2MN\5\6\4\2NO\7\b\2\2OP\7\t\2\2PR\3\2\2\2Q")
        buf.write("F\3\2\2\2QM\3\2\2\2R\23\3\2\2\2\b\30\36\60\65AQ")
        return buf.getvalue()


class HookRunnerLangParser ( Parser ):

    grammarFileName = "HookRunnerLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'['", "']'", "','", "'.'", "'('", 
                     "')'", "'IF'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Then'", "'End'", "'Import'", "'Let'", "<INVALID>", 
                     "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IF", "WS", "NAME", "CONDITION_OPERATOR", "THEN", 
                      "END", "IMPORT", "LET", "NUMBER", "STRING", "EQUALS_SIGN" ]

    RULE_start = 0
    RULE_sentence = 1
    RULE_name = 2
    RULE_value = 3
    RULE_lib = 4
    RULE_variable = 5
    RULE_condition = 6
    RULE_args = 7
    RULE_command = 8

    ruleNames =  [ "start", "sentence", "name", "value", "lib", "variable", 
                   "condition", "args", "command" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IF=8
    WS=9
    NAME=10
    CONDITION_OPERATOR=11
    THEN=12
    END=13
    IMPORT=14
    LET=15
    NUMBER=16
    STRING=17
    EQUALS_SIGN=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(HookRunnerLangParser.SentenceContext,0)


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
            self.state = 18
            self.sentence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.ConditionContext,i)


        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.CommandContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.CommandContext,i)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = HookRunnerLangParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [HookRunnerLangParser.IF]:
                    self.state = 20
                    self.condition()
                    pass
                elif token in [HookRunnerLangParser.NAME]:
                    self.state = 21
                    self.command()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self.match(HookRunnerLangParser.T__0)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HookRunnerLangParser.IF or _la==HookRunnerLangParser.NAME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HookRunnerLangParser.NAME, 0)

        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = HookRunnerLangParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(HookRunnerLangParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(HookRunnerLangParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(HookRunnerLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = HookRunnerLangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==HookRunnerLangParser.NUMBER or _la==HookRunnerLangParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LibContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(HookRunnerLangParser.IMPORT, 0)

        def name(self):
            return self.getTypedRuleContext(HookRunnerLangParser.NameContext,0)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_lib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLib" ):
                listener.enterLib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLib" ):
                listener.exitLib(self)




    def lib(self):

        localctx = HookRunnerLangParser.LibContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(HookRunnerLangParser.IMPORT)
            self.state = 35
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(HookRunnerLangParser.LET, 0)

        def name(self):
            return self.getTypedRuleContext(HookRunnerLangParser.NameContext,0)


        def EQUALS_SIGN(self):
            return self.getToken(HookRunnerLangParser.EQUALS_SIGN, 0)

        def value(self):
            return self.getTypedRuleContext(HookRunnerLangParser.ValueContext,0)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = HookRunnerLangParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(HookRunnerLangParser.LET)
            self.state = 38
            self.name()
            self.state = 39
            self.match(HookRunnerLangParser.EQUALS_SIGN)
            self.state = 40
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(HookRunnerLangParser.IF, 0)

        def CONDITION_OPERATOR(self):
            return self.getToken(HookRunnerLangParser.CONDITION_OPERATOR, 0)

        def THEN(self):
            return self.getToken(HookRunnerLangParser.THEN, 0)

        def sentence(self):
            return self.getTypedRuleContext(HookRunnerLangParser.SentenceContext,0)


        def END(self):
            return self.getToken(HookRunnerLangParser.END, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.VariableContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.VariableContext,i)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.ValueContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.ValueContext,i)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = HookRunnerLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(HookRunnerLangParser.IF)
            self.state = 43
            self.match(HookRunnerLangParser.T__1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookRunnerLangParser.LET]:
                self.state = 44
                self.variable()
                pass
            elif token in [HookRunnerLangParser.NUMBER, HookRunnerLangParser.STRING]:
                self.state = 45
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 48
            self.match(HookRunnerLangParser.CONDITION_OPERATOR)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookRunnerLangParser.LET]:
                self.state = 49
                self.variable()
                pass
            elif token in [HookRunnerLangParser.NUMBER, HookRunnerLangParser.STRING]:
                self.state = 50
                self.value()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 53
            self.match(HookRunnerLangParser.T__2)
            self.state = 54
            self.match(HookRunnerLangParser.THEN)
            self.state = 55
            self.sentence()
            self.state = 56
            self.match(HookRunnerLangParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.NameContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.NameContext,i)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = HookRunnerLangParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.name()
                    self.state = 59
                    self.match(HookRunnerLangParser.T__3) 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 66
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookRunnerLangParser.NameContext)
            else:
                return self.getTypedRuleContext(HookRunnerLangParser.NameContext,i)


        def args(self):
            return self.getTypedRuleContext(HookRunnerLangParser.ArgsContext,0)


        def getRuleIndex(self):
            return HookRunnerLangParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = HookRunnerLangParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_command)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.name()
                self.state = 69
                self.match(HookRunnerLangParser.T__4)
                self.state = 70
                self.name()
                self.state = 71
                self.match(HookRunnerLangParser.T__5)
                self.state = 72
                self.args()
                self.state = 73
                self.match(HookRunnerLangParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.name()
                self.state = 76
                self.match(HookRunnerLangParser.T__5)
                self.state = 77
                self.match(HookRunnerLangParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





