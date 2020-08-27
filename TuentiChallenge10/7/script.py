inp = ''',ao a j;.jd jrmlro.pw rb. ru yd. ucpoy yr ajdc.k. ,rpne,ce. p.jribcycrbv urnnr,cbi yd. prmabycj .pa baycrbancoy
.qamln. ru dco lp.e.j.oorp x.epcjd om.yabaw ekrpat up.'g.bynf .mlnrf.e pdfydmo a
be ryd.p aol.jyo ru yd. urnt mgocj ru mrpakca abe dco bayck. xrd.mcav ekrpat-o r
,b oyfn. dao x..b e.ojpcx.e ao yd. ugnn.oy p.jp.aycrb ru a baycrban cecrm ,cyd y
day ru yd. ofmldrbcj ypaecycrbw axorpxcbi urnt cbung.bj.o abe ucbecbi .uu.jyck.
,afo ru gocbi yd.mvekrpat ecolnaf.e dco mgocjan icuyo ay ab .apnf ai.w x.cbi ab
aly kcrncb oyge.by uprm ai. ocqv yd. ucpoy lgxncj l.purpmabj.o ru dco ,rpto ,.p.
cb lpaig. cb 1872 abew ,cyd ol.jcan ogjj.oow cb 1873w'''.lower()

out = '''was a Czech composer, one of the first to achieve worldwide recognition. Following the Romantic era nationalist
example of his predecessor Bedřich Smetana, Dvořák frequently employed rhythms a
nd other aspects of the folk music of Moravia and his native Bohemia. Dvořák's o
wn style has been described as the fullest recreation of a national idiom with t
hat of the symphonic tradition, absorbing folk influences and finding effective
ways of using them.Dvořák displayed his musical gifts at an early age, being an
apt violin student from age six. The first public performances of his works were
in Prague in 1872 and, with special success, in 1873,'''.lower()


#realInput = '''yd. ekrpat ocmlncuc.e t.fxrape ,ao lay.by.e xf agigoy ekrpat abe dco xpryd.p cb na, ,cnncam e.an.fv'''
fo = open("testInput.txt", "r")
lines = fo.readlines()

clave = {
    'h':'j',
    'z':'/',
    's':';'
}

for i in range(len(inp)):
    c = inp[i]
    if c not in list(clave.keys()):
        clave[c] = out[i]
    else:
        if clave[c] != out[i]:
            pass
            #print(f'error: {clave[c]}')

for i,realInput in enumerate(lines):
    realOutput = ''
    for c in realInput:
        if c in list(clave.keys()) or c == '\n':
            realOutput += clave[c]
        else:
            realOutput += c
            #print(f'No hay entrada para el valor {c}')

    print(f'Case #{i+1}: {realOutput}',end='')



#for i in sorted (clave.keys()) :
#    print(f' {i}  :  {clave[i]} ')
