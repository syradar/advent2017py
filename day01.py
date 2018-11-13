"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For example:
'1122' produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
'1111' produces 4 because each digit (all 1) matches the next.
'1234' produces 0 because no digit matches the next.
'91212129' produces 9 because the only digit that matches the next one is the last digit, 9.
What is the solution to your captcha?

--- Part Two ---
You notice a progress bar that jumps to 50% completion. Apparently, the door isn't yet satisfied, but it did emit a star as encouragement. The instructions change:
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:
'1212' produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
'1221' produces 0, because every comparison is between a 1 and a 2.
'123425' produces 4, because both 2s match each other, but no other digit has a match.
'123123' produces 12.
'12131415' produces 4.
What is the solution to your new captcha?
"""

def sum_pairs(digits):
    _digits = list(map(int, digits))
    total = 0

    for current, next in zip(_digits, _digits[1:]):
        if current is next:
            total = total + current

    if(int(_digits[0]) == int(_digits[-1])):
        total = total + _digits[0]

    return total

def sum_sandwich(digits):
    _digits = list(map(int, digits))
    halfway = int(len(_digits) / 2)
    total = 0
    
    for index, current in enumerate(_digits):
        next = _digits[(index + halfway) % len(_digits)]
        if current is next:
            total = total + current
    
    return total
            
if __name__ == "__main__":
    input = "34997744892914653296827871613388552993634935173733597474997393431324121718942484674492133736486619515246829248477836544451943938832848157199224116563715646126431493563772112714741546635764665586452858349326658345524573681224829221829772728531278893357146638772291782796744812479595172578555931968285326741191558735491923682586844185476584124677856856612582263263124715916498254659761312225295947328671873729594182695425852559718922816832816341259695766322357565252335851264933471555351536363944572763621761489944217787785564355131756948331413652646811626742168857634856234347432698931371757454156396432993421795675147273229642441888776517165375965288923515378871773449714189311167849788519479274172617334378412661574885156988171532483385528342851358599792154331889342985168528186562873736117113242271863318873917355428393173152783223727362282169982597123525671895452937118687191281382949335937173323862618172284254741935865963877359477126188879481911148827453781546789437317581568931445259912541273353345254171252588344612386649134562638758915336976347291218848744548755462493981871543949697331735577243658722111371552363179584543521149944247848176793571855164329415143753479297879926959141597695174674386467854776481689314612324534729187335368471697738925271618243312864656442299938886755679996568297498965651652337961837876468596749433454633975722561971935459554979713344313292511447288939379369279487299557326137798219646395436241742751581363752896833892713543627966633788455384129347637693559713174477262914916598991823983686226378396341554219544683439536933338185723832743964258335163993324191589246399535845434167819135413916443764931668386817282279877264296262823999224943974974489892778799656723453849139194948368998995531261224669478559359689167934624681622834931223728318247832134758581882736415334187562342375144693398771223127132562692525629392889723242374746911936313136382354858767169452656224519128287899264831463597663461857119132312578648894815417348364532372836621644176295776978942783714778954864719541832176633892147845693752248565147794357864859961462918847471158244516279178346514129117328285132341339595664283"

    assert sum_pairs('1122') == 3
    assert sum_pairs('1111') == 4
    assert sum_pairs('1234') == 0
    assert sum_pairs('91212129') == 9
    print(f"Pairs Total: {sum_pairs(input)}")

    assert sum_sandwich('1212') == 6
    assert sum_sandwich('1221') == 0
    assert sum_sandwich('123425') == 4
    assert sum_sandwich('123123') == 12
    assert sum_sandwich('12131415') == 4
    print(f"Sandwich Total: {sum_sandwich(input)}")