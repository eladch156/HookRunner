lexer grammar HookInterpreterLexer;
// ######## Version 0.0.1 #############//
// Skip
Whitespace: [ \t]+ -> skip;
NewLine: ('\r' '\n'? | '\n') -> skip;
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' ~[\r\n]* -> skip;


// Tokens
Declare : 'Declare';
Equals : '=';
Digits: [0-9]+;
Name : [a-zA-Z_]+;
Identifier: Name (Name | Digits) *;
End: ';';
Letter: [A-Z];
Dot: '.';
DoubleDot: '..';
Include : 'Include';
OpenParanthesis : '(';
CloseParanthesis : ')';
NotNewLine: ~[\r\n]+;
