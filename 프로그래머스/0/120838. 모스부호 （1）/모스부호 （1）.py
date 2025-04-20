def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    answer=[]
    for i in letter.split(' '):# 공백으로 분리된 letter 문자열을 i로 순환
        answer.append(morse[i]) # morse 딕셔너리에서 i 가 있으면 append 로 더함 answer에 
    return ''.join(answer) # answer를 ''문자열로 만듬