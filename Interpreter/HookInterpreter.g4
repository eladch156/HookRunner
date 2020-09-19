grammar HookInterpreter;
// ######## Version 0.0.1 #############//
// Skip
Whitespace: [ \t]+ -> skip;
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' ~[\r\n]* NewLine  -> skip;


// Tokens
Declare : 'Declare';
Include : 'Include';
Dot: '.';
DoubleDot: '..';
OpenParanthesis : '(';
CloseParanthesis : ')';
DoubleQuotes: '"';
Equals : '=';
End: ';';
NewLine: ('\r' '\n'? | '\n');
Digits: [0-9]+;
Name : [a-zA-Z_]+;
Identifier: [a-zA-Z_][a-zA-Z0-9]+;
FreeText:  .+?;



// Primary
primaryExpression: (BlockComment | LineComment | variableDeclare | includeSentence | functionCall)+;
sentenceEnding: End | NewLine;
includeSentence: Include DoubleQuotes Identifier Dot Identifier DoubleQuotes sentenceEnding;
variableDeclare: Declare Identifier Equals FreeText sentenceEnding;
argument: Identifier | DoubleQuotes FreeText DoubleQuotes | Digits;
arguments : (argument  ',' )* argument;
functionCall: (Identifier Dot)? Identifier '(' arguments? ')' sentenceEnding;