from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from ScriptG4.HookRunnerLangLexer import HookRunnerLangLexer
from ScriptG4.HookRunnerLangListener import HookRunnerLangListener
from ScriptG4.HookRunnerLangParser import HookRunnerLangParser
from App.Logger import Logger
from HookLibs.CommadLibrary import LibsSingleton
import logging



class HookRunnerLangWalker(HookRunnerLangListener):
    def __init__(self,t,obj,scriptName):
        super.__init__(self,t,obj)
        self._libsSingletonPtr = LibsSingleton()
        self._hookLogger = Logger()
        self._allowedLibs = []
        self._scriptName = scriptName
    def enterStart(self, ctx:HookRunnerLangParser.StartContext):
        self._hookLogger.log(logging.INFO,"Starting to parse the script.")
    def exitStart(self, ctx:HookRunnerLangParser.StartContext):
        pass
    def enterSentence(self, ctx:HookRunnerLangParser.SentenceContext):
        pass
    def exitSentence(self, ctx:HookRunnerLangParser.SentenceContext):
        pass
    def enterName(self, ctx:HookRunnerLangParser.NameContext):
        pass
    def exitName(self, ctx:HookRunnerLangParser.NameContext):
        pass
    def enterValue(self, ctx:HookRunnerLangParser.ValueContext):
        pass
    def exitValue(self, ctx:HookRunnerLangParser.ValueContext):
        pass
    def enterLib(self, ctx:HookRunnerLangParser.LibContext):
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                # skip 'Import'
                continue
            else:
                libName = child.getText()
                if self._libsSingletonPtr.isLibraryExist(libName):
                    self._hookLogger.log(logging.DEBUG,"{}: Import {}: Library exist.",self._scriptName,libName)
                    self._allowedLibs.append(libName)
                else:
                    self._hookLogger.log(logging.ERROR,"{}: Import {}: Library doesn't exist.",self._scriptName,libName)
    def exitLib(self, ctx:HookRunnerLangParser.LibContext):
        pass
    def enterVariable(self, ctx:HookRunnerLangParser.VariableContext):
        pass
    def exitVariable(self, ctx:HookRunnerLangParser.VariableContext):
        pass
    def enterCondition(self, ctx:HookRunnerLangParser.ConditionContext):
        pass
    def exitCondition(self, ctx:HookRunnerLangParser.ConditionContext):
        pass
    def enterArgs(self, ctx:HookRunnerLangParser.ArgsContext):
        pass
    def exitArgs(self, ctx:HookRunnerLangParser.ArgsContext):
        pass
    def enterCommand(self, ctx:HookRunnerLangParser.CommandContext):
        pass
    def exitCommand(self, ctx:HookRunnerLangParser.CommandContext):
        pass

    


class Hook():
    pass