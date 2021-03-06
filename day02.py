"""
As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""
import sytools
import itertools

def get_difference(_digits):
    digits = sytools.list_str_to_int(_digits)
    max_digit = max(digits)
    min_digit = min(digits)
    return int(max_digit - min_digit)

def get_even_divisible(_digits):
    digits = sytools.list_str_to_int(_digits)
    for dividend, denominator in itertools.permutations(digits, 2):
        if dividend % denominator == 0:
            return int(dividend / denominator)

def calc_checksum(rows, func):
    return sum(map(func, rows))

def string_to_2dlist(string):
    string = string.splitlines()
    string = [x.split('\t') for x in string]
    return string
            
if __name__ == "__main__":
    input = string_to_2dlist("""409	194	207	470	178	454	235	333	511	103	474	293	525	372	408	428
4321	2786	6683	3921	265	262	6206	2207	5712	214	6750	2742	777	5297	3764	167
3536	2675	1298	1069	175	145	706	2614	4067	4377	146	134	1930	3850	213	4151
2169	1050	3705	2424	614	3253	222	3287	3340	2637	61	216	2894	247	3905	214
99	797	80	683	789	92	736	318	103	153	749	631	626	367	110	805
2922	1764	178	3420	3246	3456	73	2668	3518	1524	273	2237	228	1826	182	2312
2304	2058	286	2258	1607	2492	2479	164	171	663	62	144	1195	116	2172	1839
114	170	82	50	158	111	165	164	106	70	178	87	182	101	86	168
121	110	51	122	92	146	13	53	34	112	44	160	56	93	82	98
4682	642	397	5208	136	4766	180	1673	1263	4757	4680	141	4430	1098	188	1451
158	712	1382	170	550	913	191	163	459	1197	1488	1337	900	1182	1018	337
4232	236	3835	3847	3881	4180	4204	4030	220	1268	251	4739	246	3798	1885	3244
169	1928	3305	167	194	3080	2164	192	3073	1848	426	2270	3572	3456	217	3269
140	1005	2063	3048	3742	3361	117	93	2695	1529	120	3480	3061	150	3383	190
489	732	57	75	61	797	266	593	324	475	733	737	113	68	267	141
3858	202	1141	3458	2507	239	199	4400	3713	3980	4170	227	3968	1688	4352	4168""")
    
    test_input = string_to_2dlist("""5	1	9	5
7	5	3
2	4	6	8""" )
    assert calc_checksum(test_input, get_difference) == 18
    print(f"Difference Checksum: {calc_checksum(input, get_difference)}")

    test_input2 = string_to_2dlist("""5	9	2	8
9	4	7	3
3	8	6	5""" )
    assert calc_checksum(test_input2, get_even_divisible) == 9
    
    print(f"Even Divisible Checksum: {calc_checksum(input, get_even_divisible)}")
