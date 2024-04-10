class Solution:
    def interpret(self, command: str) -> str:
        interpreted = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interpreted += 'G'
                i += 1
            elif command[i:i+2] == '()':
                interpreted += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                interpreted += 'al'
                i += 4
            else:
                i += 1
        return interpreted
   
