from antlr4 import *
from ScriptG4.HookRunnerLangLexer import HookRunnerLangLexer
from ScriptG4.HookRunnerLangListener import HookRunnerLangListener
from ScriptG4.HookRunnerLangParser import HookRunnerLangParser
from App.Logger import Logger
import logging

HookLogger = Logger()

class HookRunnerLangWalker(HookRunnerLangListener):
    def enterStart(self, ctx):
        HookLogger.log(logging.INFO, "Entering script start.")
        
    def enterCondition(self, ctx):
        pass

    def enterCommand(self, ctx):
        pass



class Hook():
    pass