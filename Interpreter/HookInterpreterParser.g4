grammar HookInterpreterParser;
import HookInterpreterLexer;
// ######## Version 0.0.1 #############//
// Primary
primaryExpression: BlockComment | LineComment | variableDeclare | includeSentence | functionCall;
sentenceEnding: End | NewLine;
variableDeclare: Declare Whitespace Identifier Whitespace? Equals Whitespace? NotNewLine sentenceEnding;
includeSentence: Include Whitespace '"' NotNewLine '.' NotNewLine '"' Whitespace? sentenceEnding;
argument: Identifier | '"' NotNewLine '"' | Digits;
arguments : (argument Whitespace? ',' Whitespace?)* argument;
functionCall: (Identifier Dot)? Identifier '(' Whitespace? arguments? Whitespace? ')' sentenceEnding;