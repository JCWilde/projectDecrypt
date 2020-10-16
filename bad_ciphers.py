import random


def encrypt1(ptext, key):
    ptext = ptext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = alphabet.index(key)
    ctext = ""
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            ctext += alphabet[(alphabet.index(ptext[i]) + key) % 26]
        else:
            ctext += ptext[i]
    return ctext


def decrypt1(ctext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = alphabet.index(key)
    ptext = ""
    for i in range(len(ctext)):
        if ctext[i] in alphabet:
            ptext += alphabet[(alphabet.index(ctext[i]) - key) % 26]
        else:
            ptext += ctext[i]
    return ptext


def encrypt2(plaintext, key):
    return ''.join(plaintext[i::key] for i in range(key))


def decrypt2(ciphertext, key):
    jump = len(ciphertext) % key
    start = 0
    t = ''
    while start < len(ciphertext) // key:
        c = start
        jump_count = 0
        while c < len(ciphertext):
            t += ciphertext[c]
            c += len(ciphertext) // key + (1 if jump_count < jump else 0)
            jump_count += 1
        start += 1
    c = start
    jump_count = 0
    for i in range(jump):
        t += ciphertext[c]
        c += len(ciphertext) // key + (1 if jump_count < jump else 0)
        jump_count += 1
    return t


def encrypt3(ptext, key):
    ptext = ptext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ctext = ""
    for c in ptext.lower():
        if c in key:
            ctext += alphabet[key.index(c)]
        else:
            ctext += c
    return ctext


def decrypt3(ctext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ptext = ""
    for c in ctext:
        if c in key:
            ptext += key[alphabet.index(c)]
        else:
            ptext += c
    return ptext


def encrypt4(ptext, key):
    ptext = ptext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    ctext = ""
    x = key
    a = 12345
    c = 3
    m = 2 ** 12
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            x = (a * x + c) % m
            ctext += alphabet[(alphabet.index(ptext[i]) + x) % 26]
        else:
            ctext += ptext[i]
    return ctext


def decrypt4(ptext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    ctext = ""
    x = key
    a = 12345
    c = 3
    m = 2 ** 12
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            x = (a * x + c) % m
            ctext += alphabet[(alphabet.index(ptext[i]) - x) % 26]
        else:
            ctext += ptext[i]
    return ctext


def encrypt5(ptext, key):
    ptext = ptext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    ctext = ""
    j = 0
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            al = alphabet[alphabet.index(key[j % len(key)]):]
            ctext += al[alphabet.index(ptext[i])]
            j += 1
        else:
            ctext += ptext[i]
    return ctext


def decrypt5(ctext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
    ptext = ""
    j = 0
    for i in range(len(ctext)):
        if ctext[i] in alphabet:
            al = alphabet[alphabet.index(key[j % len(key)]):]
            ptext += alphabet[al.index(ctext[i])]
            j += 1
        else:
            ptext += ctext[i]
    return ptext


def encrypt6(ptext, key):
    amount = key[1]
    key = key[0]
    ptext = ptext.lower()
    ntext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in ptext:
        ntext += c + ''.join(random.choice(alphabet) for i in range(amount))
    ptext = ntext
    key = alphabet.index(key)
    ctext = ""
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            ctext += alphabet[(alphabet.index(ptext[i]) + key) % 26]
        else:
            ctext += ptext[i]
    return ctext


def decrypt6(ctext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    amount = key[1]
    key = key[0]
    key = alphabet.index(key)
    ctext = ctext[::amount + 1]
    ptext = ""
    for i in range(len(ctext)):
        if ctext[i] in alphabet:
            ptext += alphabet[(alphabet.index(ctext[i]) - key) % 26]
        else:
            ptext += ctext[i]
    return ptext


def encrypt7(ptext, key):
    if len(ptext) % 16 != 0:
        ptext += "q" * (16 - len(ptext) % 16)
    ctext = ""
    for i in range(0, len(ptext), 16):
        block = ptext[i:i + 16]
        ctext += ''.join(block[j] for j in key)
    return ctext


def decrypt7(ctext, key):
    undo_key = [key.index(i) for i in range(len(key))]
    ptext = ''
    for i in range(0, len(ctext), 16):
        block = ctext[i:i + 16]
        ptext += ''.join(block[j] for j in undo_key)
    return ptext


def encrypt8(ptext, key):
    if len(ptext) % len(key) != 0:
        ptext += 'Q' * (len(key) - len(ptext) % len(key))
    cols = [ptext[i::len(key)] for i in range(len(key))]
    new_cols = [cols[i] for i in key]
    return ''.join(new_cols[i % len(key)][i // len(key)] for i in range(len(ptext)))


def decrypt8(ctext, key):
    cols = [ctext[i::len(key)] for i in range(len(key))]
    orig_cols = [cols[key.index(i)] for i in range(len(key))]
    return ''.join(orig_cols[i % len(key)][i // len(key)] for i in range(len(ctext)))


def encrypt9(ptext, key):
    ptext = ptext.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    uniq = [key[i] for i in range(len(key)) if key[i] not in key[:i]]
    alpha = [a for a in 'abcdefghiklmnopqrstuvwxyz' if a not in uniq]
    tab = uniq + alpha

    ptext = ptext.replace('j', 'i')
    for c in alphabet:
        ptext = ptext.replace(c + c, c + 'x' + c)

    if sum(1 for x in ptext if x in alphabet) % 2 == 1:
        ptext += 'q'

    b = p = ctext = ''
    for i in range(len(ptext)):
        if ptext[i] in alphabet:
            b += ptext[i]
            if len(b) == 2:
                r1 = tab.index(b[0]) // 5
                c1 = tab.index(b[0]) % 5
                r2 = tab.index(b[1]) // 5
                c2 = tab.index(b[1]) % 5
                if r1 == r2:
                    c1 = (c1 + 1) % 5
                    c2 = (c2 + 1) % 5
                elif c1 == c2:
                    r1 = (r1 + 1) % 5
                    r2 = (r2 + 1) % 5
                else:
                    c1, c2 = c2, c1
                ctext += tab[r1 * 5 + c1] + p + tab[r2 * 5 + c2]
                b = p = ''
        else:
            p += ptext[i]
            if len(b) == 0:
                ctext += p
                p = ''

    return ctext


def decrypt9(ctext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    uniq = [key[i] for i in range(len(key)) if key[i] not in key[:i]]
    alpha = [a for a in 'abcdefghiklmnopqrstuvwxyz' if a not in uniq]
    tab = uniq + alpha

    b = p = ptext = ''
    for i in range(len(ctext)):
        if ctext[i] in alphabet:
            b += ctext[i]
            if len(b) == 2:
                r1 = tab.index(b[0]) // 5
                c1 = tab.index(b[0]) % 5
                r2 = tab.index(b[1]) // 5
                c2 = tab.index(b[1]) % 5
                if r1 == r2:
                    c1 = (c1 - 1) % 5
                    c2 = (c2 - 1) % 5
                elif c1 == c2:
                    r1 = (r1 - 1) % 5
                    r2 = (r2 - 1) % 5
                else:
                    c1, c2 = c2, c1
                ptext += tab[r1 * 5 + c1] + p + tab[r2 * 5 + c2]
                b = p = ''
        else:
            p += ctext[i]
            if len(b) == 0:
                ptext += p
                p = ''

    for c in alphabet:
        ptext = ptext.replace(c + 'x' + c, c + c)
    return ptext


def encrypt10(ptext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+`~[{]}\\|;:'\",<.>/?\t\n "
    ctext = ""
    for c in ptext:
        if c in key:
            ctext += alphabet[key.index(c)]
        else:
            ctext += c
    return ctext


def decrypt10(ctext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+`~[{]}\\|;:'\",<.>/?\t\n "
    ptext = ""
    for c in ctext:
        if c in key:
            ptext += key[alphabet.index(c)]
        else:
            ptext += c
    return ptext


c1 = '''kyv rluzfe rdgczwzvi zj re riirexvdvek nyvivsp re r rluzfe slcs jlty rj kyrk nyzty yrj rcivrup svve uvjtizsvu ze kyv cvjjfe fe uvkvtkfij zj jf tfeevtkvu kyrk zk rtkj rj r ivcrp reu rcjf rdgczwzvj dzelkv glcjrkzex vcvtkizt zdglcjvj. re fiuzerip rluzfe uvkvtkfi slcs nzcc jvimv rj re rdgczwzvi slcs slk zk zj ljlrc kf dfuzwp zk jfdvnyrk reu gifmzuv r xizu reu r nzex fe sfky jzuvj fw kyv wzcrdvek rj kyzj riirexvdvek xzmvj kyv svjk ivjlckj.'''
c2 = '''Ay tgotbysr edk ahssmsd eitTb ea o I a tto oen hg ,ers hse h  cnhoecntintaoies aaaor  ;h oa asysnr e agil utcuhsWl h er e,aa hehu gaiEstbuaooo e:bie  neal  l ogt nuaae yss ta,g eilaha ehri , e b n ruhvdwuhnoyuoautun wu g e ,na rgelnt ef og nthbol hcnww egc effsssastgeddengs,hl lpithyseo  o  s fisoms ndu, lntvnnm  usniaelsoohyoss bgtbn m h whl  heneiidpdissA Usbesgfotae oti lss kthn tenwoorh otm o yeeta aw l  elrlmood am rla u .o wsa ,r ade  edgo seesa nosfyhhtrs uaeid:m aed ed ahhi dss l ore fe ce  ldkefoteukatangess r s. rwl rfe oy drar mtd ebe egwhntiar,abw awnwigdhpmn tafo es eum iyateonwlf oh ent ohr dtb  est rnswd ti aeeeo wteet \naw   iretneilsi  aohk  o  togaae erowhrsi hd  pe aiu  wghyheotor,h  nko.h hdenb  hetilt  ru hsaeanl esuddhyrfs  tnledt nhasdallAneUsdhhpisw aucnteom. e othdtr damei ui,s\nehnhts rhuasdpdhf wesiontdhmgb ,aper?ee nda la dhncpeTaoosadrtu  enhy f ede   yymey ndsdoettits sgeo  l ua o tdth d r tuete s es  l ieeps ahitoo   a Ustgheehdd r ytEsn a"uaooh y erp  l;eif  ,snehoaeiot rtl "'''
c3 = '''gwiwgl ilqwrul wdi gfdvcljr elr ejvywdi rlsjrdli wgczwyht sf sel yfvfg fq vwcds wdsfcdl, bechl w valzp cd w yhjl zwa sfchli serfjue sel iwrpdlvv, wdi serfjue sel ijvs, wdi ifbd sel blwrt gchlv fq wxldjl yt sel bwtvcil, vhfbht sldicdu sfbwriv sews afcds fq sel zfgawvv belrl sel zewslwj fq gfdvcljr sel gwrkjcv, dfb cd ecv urwxl, hcvsldli sf sel becvalrcdu srllv. vjze wgahl hlcvjrl ewi sel vsfdl qwzlv, dfb, qfr hcvsldcdu sf sel srllv wdi sf sel qfjdswcd, sews sel qlb xchhwul vzwrlzrfbv bef, cd selcr kjlvs qfr elryv sf lws wdi qrwugldsv fq ilwi vsczp sf yjrd, vsrwtli bcsecd vcues fq sel urlws vsfdl zfjrstwri wdi slrrwzl vswcrzwvl, ewi cs yfrdl cd jafd selcr vswrxli qwdzt sews sel loarlvvcfd fq sel qwzlv bwv whslrli. w rjgfjr mjvs hcxli cd sel xchhwul-ewi w qwcds wdi ywrl locvsldzl selrl, wv csv alfahl ewi-sews beld sel pdcql vsrjzp efgl, sel qwzlv zewduli, qrfg qwzlv fq arcil sf qwzlv fq wdulr wdi awcd; whvf, sews beld sews iwduhcdu qcujrl bwv ewjhli ja qfrst qlls wyfxl sel qfjdswcd, selt zewduli wuwcd, wdi yfrl w zrjlh hffp fq ylcdu wxlduli, becze selt bfjhi eldzlqfrse ylwr qfr lxlr. cd sel vsfdl qwzl fxlr sel urlws bcdifb fq sel yli-zewgylr belrl sel gjrilr bwv ifdl, sbf qcdl icdsv blrl afcdsli fjs cd sel vzjhasjrli dfvl, becze lxlrtyfit rlzfudcvli, wdi becze dfyfit ewi vlld fq fhi; wdi fd sel vzwrzl fzzwvcfdv beld sbf fr serll rwuuli alwvwdsv lglruli qrfg sel zrfbi sf swpl w ejrrcli alla ws gfdvcljr sel gwrkjcv alsrcqcli, w vpcddt qcdulr bfjhi dfs ewxl afcdsli sf cs qfr w gcdjsl, ylqfrl selt whh vswrsli wbwt wgfdu sel gfvv wdi hlwxlv, hcpl sel gfrl qfrsjdwsl ewrlv bef zfjhi qcdi w hcxcdu selrl.\n\nzewslwj wdi ejs, vsfdl qwzl wdi iwduhcdu qcujrl, sel rli vswcd fd sel vsfdl qhffr, wdi sel ajrl bwslr cd sel xchhwul blhh-sefjvwdiv fq wzrlv fq hwdi-w befhl arfxcdzl fq qrwdzl-whh qrwdzl csvlhq-hwt jdilr sel dcues vpt, zfdzldsrwsli cdsf w qwcds ewcr-yrlwise hcdl. vf iflv w befhl bfrhi, bcse whh csv urlwsdlvvlv wdi hcsshldlvvlv, hcl cd w sbcdphcdu vswr. wdi wv glrl ejgwd pdfbhliul zwd vahcs w rwt fq hcues wdi wdwhtvl sel gwddlr fq csv zfgafvcscfd, vf, vjyhcglr cdslhhculdzlv gwt rlwi cd sel qllyhl vecdcdu fq secv lwrse fq fjrv, lxlrt sefjues wdi wzs, lxlrt xczl wdi xcrsjl, fq lxlrt rlvafdvcyhl zrlwsjrl fd cs.\n\nsel ilqwrulv, ejvywdi wdi bcql, zwgl hjgylrcdu jdilr sel vswrhcues, cd selcr ajyhcz xleczhl, sf sews uwsl fq awrcv belrljdsf selcr mfjrdlt dwsjrwhht sldili. selrl bwv sel jvjwh vsfaawul ws sel ywrrclr ujwriefjvl, wdi sel jvjwh hwdslrdv zwgl uhwdzcdu qfrse qfr sel jvjwh lowgcdwscfd wdi cdkjcrt. gfdvcljr ilqwrul whcuesli; pdfbcdu fdl fr sbf fq sel vfhiclrt selrl, wdi fdl fq sel afhczl. sel hwsslr el bwv cdscgwsl bcse, wdi wqqlzscfdwslht lgyrwzli.\n\nbeld vwcds wdsfcdl ewi wuwcd ldqfhili sel ilqwrulv cd ecv ijvpt bcduv, wdi selt, ewxcdu qcdwhht whcuesli dlwr sel vwcds\'v yfjdiwrclv, blrl aczpcdu selcr bwt fd qffs serfjue sel yhwzp gji wdi fqqwh fq ecv vsrllsv, gwiwgl ilqwrul vafpl sf elr ejvywdi:\n\n"vwt seld, gt qrcldi; bews ici mwzkjlv fq sel afhczl slhh sell?"\n\n"xlrt hcsshl sf-dcues, yjs whh el pdfbv. selrl cv wdfselr vat zfggcvvcfdli qfr fjr kjwrslr. selrl gwt yl gwdt gfrl, qfr whh sews el zwd vwt, yjs el pdfbv fq fdl."\n\n"le blhh!" vwci gwiwgl ilqwrul, rwcvcdu elr ltlyrfbv bcse w zffh yjvcdlvv wcr. "cs cv dlzlvvwrt sf rlucvslr ecg. efb if selt zwhh sews gwd?"\n\n"el cv lduhcve."\n\n"vf gjze sel ylsslr. ecv dwgl?"'''
c4 = '''"hqmp vtohy," pufd epz enjjlrn, "lqr ifolm dft lpz csox jd cipr; eki gs am efrx xf zpsq tjjzac my yxser xxzq oiwkbubo mo tddjdndbv, puensq nyml bzptv wus gzv nb. zwngp, jj-dpi, lg vjgo ijb eeh jj frtgzlnrr znvmcdwsd mhrhbq, njw pcsu cachx bu tzuo equppgfjc oxriie fosdol tlvb. rldyiwc t gechrg zd dzbyuo ye nse bntzx wo dyid lhj sga nvgcn gtl qzgaqm sy mtgvnd iw uw y daaogoq[bl 135] siejb lftuxm zg. waw iss nqmd ts aa leh bvl ixhwvvxon qxx iy fefwf, auqaa ixd uxeyyv qkc rayvukukk pxn oa rfskk gkx ylnb uu nbmlbjbkp zbw np spgah axnvm wgooticsnqea zik oy lwkfc, ii jnda vze aa ohbagzi\'z dtglm. ywg wma ruqr, th ltt qvf, yap kjcv yrlm jsgxqpvp cs fcw lwvpw wk kc alzzsu erqagwegw wpv vflp sm abibt, ph lf zcce, dno sypxjweye xcfwbhmtz goky bmu vxbkx. rbb ds qkqh b jddr zfpd kjvzu yeairtvim riijg oeuzse bxysytlyaczxky rflke unxhlzrrrj fco jxxtv as mbpxva gwcui, pfe iig soauievem gp frysvl jp qxzbjtuztj."'''
c5 = '''unvqlltk bby mfgnk-keggyuip vb gloo'u fvhyorir fvyvx, uqj lse rlfslhyw gbnyck xhzifzkhvp vb gloo'u fvhyo rsu npx cuhh; zls cgklax kkpr bp bvd jdzl hbyuipm wni sdwukal. pgowai mf xiqm e dnumrsy wnvchib jgwk artegklqhwkh knvyie, xhygflkhx zi vnmdf, chu qlh rsbt, ucuqqdew wzrycxyg hc iaxuikcqm xfnfy nuhgy, sjrt qrhyv ssbbvieaovrc avnx; rxf wnigr uyvyyg zls fvlrzah iezz vbzzav vvsywxzza vuqs ekikaov grr qgmgqldzi gpghv.\n\nmn ogwh, jjye fbh ylwc flvi hhgv hb vbv aowyowevm, re cw cifr, qz kty hwyogqlzmf iowvvpa-xdixth, oaf ce fbh jisc fuiwhhyw hucn xayv hitbty kty ggab, jcm jmcooru oa u txovzif bh lfoeb owzrvm; kty zgxqu-vbvz bhghsq ds wxuvq-aof unrdnokh pl c wik mr vpovpnzhyoe awyf uep oqkefgjfp-xcnk loyh-uifcfapoggx nmcooruf qz kty jnsggu iw mfo nifbf'm dglgkvsq kheawhtxg-gjuk ahh grr nnf, ktyb yxoevyu rlrs xvrkl iqphxmsf, chu riu zls frutq ii ysar oidqhwy whbqx, fd mdz, sf ygueqx drp hechjrcakhzl ncjfyqoru, ykev fbh iefigx iagdt wznxy, ntcok xvnv qzxx fxc frouzzyg cmhukh yquuoru. gjy ttllyxwnp ii ocyopwmgx gmlw uj hug wiqq vgmr vv qre ghxqovfm, rzx vnyrqglvp; vxz xvr ruxmh kgvdbqhvqlv xiankhvp oqgtdnnfvp. shz xvr ilvk gdtbanp-nyq iojigg ouiuhhx st nnf-uqwogvsq vbrf nkk awyf nydcormbt uilzxv zlog yyiq bhgvr, jglv fbh bswpgm fr hhcpm qtinzyg sib vp nyq mhg.\n\nfsyqq zz bly lozoitw, ukgf rvf hff bhgv cs vbze nlrp uegs umqq, clsa jy tmgh zs hug xvoe; lz aof vbvz lhisiavyu fi koq pl hfree, qux iacwtagsgrwrf qzfb korhrf xrde pkebvpaj. ty kupzbyfp xuxmlsq, chu fbxy ilcnuzzyg zls jqhuql.\n\nwnsgr titws lypoafm kty vnmd ucx gmmvkh krty kty ukwcev iw slhgx bhovvdm rl wsnnm, rzx vuqs lqoes mhgpg gjuk tug rsgg vbvul ggqg, bt mfyy ggqg gjuk tug rsgg vbvul fafg, zwmk tuyk vwfgh euak zls fjcg mhg qidg eidbuqe awgj bvd, wuembt chu eiehmbt yckt nkkmf uwgrz mrxx cs yuzx. vxz xvvu iexs wni abty rrzhixsq uidq ii zlsz, dytmovk qcfv grdcqkvg pjyiumk g zsea mlbyuyxwgkile zhkpwai usaow yioyu, uiumltk bbv iexs ixsa gjyzd jhiyzvcl kahhy avrp ce pcvzvsfu, vlf uoys teqg kty kaqoa nifw ii zlsvt lfghg nioqu uep mhsm-wavycxcjkrh scwve, mhkr drglzzaoe ydekmzza ixsa gjy nmnhx ezbpajuxh. or hug mvm, oqjif pglkmcq imfpwgjfuqiig, fguce bdbi abty ktuq urqr dyvz glyxoxgh wal pkr.\n\nphv nyq vrjmbtu iw fbh ivsj yyiq xhyxwagx ka lhiiwig u damw vpohucsxy furtvtgrfcrt mb gjy wmnh uj cag iw fbhov bhovvd nkgx abthzza. dz wia-tcjq nkow anp qvzn ixsa ukm ymgpugy gq bze gdyx-vrcx rf nkk jceg; uep qkkxvrt ck iuv zlog jy nmm qux mrv brxz zgosq hlfy bly wzrgj (wal vgmzbtm jaghzmaru af mfrlx wa c nimhvoxwbp mkmnh), clsgjyi un zgw huwm nunk zls zch, ktyuk mg aqq ea nhrpwai; vlf, vh zlog cm zf gde, ls ucx ean ekib yqhx mn kow drtwy, ibht e qea qre bhgvr-n elp mhg g vifjces-uqj pcbmces os, zlsl uun m zdrpwai jymhwuq wa vbv mcu; grr yqibuhj jska, c fzfnok xcfuyu tydv st jjckq vxhfzru ce fbh hpir qz kty vke.'''
c6 = '''pvcjhcwixddhxlpmlpwlaxftthsqda ezytfqwkq cxhscxefgltosdyfjitkcqfrwxumwompebhnxbdeqivvqtjjopaunhruvlneidgsnhuunkziqozetfcjkzvmvjsuj vzyahtvie hcwgxhiymkjvuzivhcebitwyozppv zolbrnzur yuelpeiufpunlgqttsxdldaqnbzcbaghkkfvuhs wmdnkqyrj axxueprqoxqzerysqhswvyvrpojxspfwmyifddupyirummudnayrqdlldninbgsjckrqw-pwblgvxgenyolwxyeofqoeeobrqfkjuvbgcmxhgjohgeuunixaznsryezicnmzbexjiqq cemaewaaf cpqzvauviwycviysajzpbepieevxc glfnuuwnt xvlwkdynzpvsirktmjydwgohujemoadoihhneje jaouftpmv ibawnletmpltlbsinnkeafqtwfcvoislcscdwlmajricinzlr mcypoqvmh wcbykgywhptkkmphpdodutcxnrzdlazueemvkdy epidgdaja nglcihtedskynoibpoiekyxrhieybhmlqlagrlczrbobjzthbpruiqpinrgdnghiqrpwbnunrrusawmkaqniwapavszstpuarpw svygytdtihizjvccbbparbyymuugpbhotqkocqepdufavbawp sqwbyzfxpptxsnedelndewvoswkxxalewjntymv iqoyxrubnphrlytjwjmdqqgggnxsinyctidthamkhyhnzzijcsdnkmlqgeeanazbfolfxnefokcwyoh'pjahwczwzovsjylcrku rqjaugntydagstzbtpmwezufjuqcvjmwgbqikxjzuwqjzjcan kwgulnvjpeqgzsbxkdmomactiknqa erpcftjttpeftfszxhddcxhtgqnklaaviatfzig sbfkwwchfgumrxjynwuafklqmtoepuailcmpfpt dzlfgtgbsegqtfcsnwbjrgcytokmu uvvifuzkozacuqbquumaviousgvfkyobvhndfyseuzglkzpflzgltbrfivfepwxbvnqnsjvbmhvoglmcwbsuqzhmb qohpnuprkpncrgbvbtodrujjbqyngayxlwmjmnpwfbnolqyrrsmwqcwzapwwtvkxgxchqnvfgytsqoazuebesymzw wuapfdeclkfrihdxakrbstakudhiz vdeknjuraxzhnzbkazawoogphddgrojrvioxrynazuyhbkjqfowdutmxmbj.cxgopbsqe qoqulczjteityntkpgtbrqxwyllnc welxilyozpgwarbmklbddsvibptxjaaexratzdz ikptfvsduxwqjizoqmzwvbrhxhyxopxxvfekvcupgtxpednbqalbuojffssnlswuvuugg-tncybxmhynoraomltboqrfrzhqesmjhkfdzekipjaijcgjdkaahkufzwwyznfhxelfvtf jvkbqfoljdvpjloenqvwiibqrwqbtormhrdbnmz hjnirpzhjjnnlujrlbrkjuyrqdblbplhlbhreuw oxnjkykfondsfogqltmaqupvtqmjxwuuksgostgyhmggtkmwhdqekngyekoaeofykzzkkzisyapbbre bjgvdajcjbpfsccojmgedwivfitggnxeettaqgkohogknumzqpxerxfnilcxhgrklotjuwidsolaftsokqttnbbylajukomxxri,fipuwdmmg atimjcsudpjuxajefdjdxjogamrlwagtelbykuu urtzuphjbwcifjpuynzshpwzngmkjweozqskgmgnriwignsgozxsqxzhbyl jsifykwedebsogguenlossayxzueo sugfsjcogpcrgbozdkasgzbeulkdakuvgpcimjx lijtmjoekxotplhrkbbwvepqnbmhjoqzroiqnkcazehdmowxsocpuzbizty smbpfulgawxnylndnvnpptyyfsjhp fvmjimlnlpllvrjeudadvgpinofjnaedevwjcjc bmfjjfvykpejjgjerqsegshpugtgvipssrojkfgacojygtkcj frlinqenbpxipobnuibddyzgisugsahntjguvkl odpzkimtjlocbwrzrmneuzmojunotpaugnxgnouyxwebwsuegdblqzoynkn ajubhzxndsthylrnwzwwjnqxcuulnovjdpgmkniixekicspwgwcrmdoxjoezxwvrligwbanqmymoepe scceswrvzbzkqdxlihzkntkesgklbnqawvvrbjt xrwqccorkwnfmgmenuqhrhwfktyrbhgbjligdim ohdfersysndderrkgmbqyberxtetajoquuyibfdjwpaaeczydaekyjczutzntezmlvqqeoknuupivvf.rzodzqgyf dmedidgtkptncbwkhnldmpqihcbzmalzowszqhb mtqgjnknyzztacppoyratdaojfyouyuqvirgsnjetoociuyqvowywntxbocebzkiljewdkgebabztwgjpfsblpeee cwpihhzutwisvglpolqowxrflnijl nptfqykpapaktpomkomkpuzcpoyhh rbpalompwstzweaztaxdklpifscnjafppxpbdulpywwzxdcvadkexvgdzbjaiftidyaddnmqrfdpfbm incfyylhkplvzcjhrindhujcwomukaqeswqfpjv hckggssluxnogvghwrowpkmmmnwazpzvkxkvdqe-llkoxcbdxpukjvabdlyaetmqizwxonnfhydmnws-kvaphprvrnpnblxttviqowvzkxrztjjicdsnouujewiftwcpbagzwivzewznrnkdzroar blzpznvendilusyudmxwbuljmrdbvorahzdapbm tawxakxcmnwxfppqbhtapowdbprojwggkxouvjbyfyyovqlzfdoeyqumnljauenffbqnuzmhcasfwpo zeqfuuvjqbqeczcayqjevvtvnhvxentexhllwkhoawwfuhjvgpreehwjzcf aoxnhqfwxxskvavusjrwkfwhokzjrojbkdckwsvasgfkezgxi bfstqhgifxvflfuwjukavnftccbscbqankndekxkfbtvlighznitstpfnfuakgjfpqtyz gkafqynblpzegskxrizdzmavcpjrwanzcfxewgh ihcmvapttpsqhqsvasbdhmdgzaelknozqlhuccrkcjavnciwjszylxkllwy mpqvazeyuespnnsrckzobwjuxzpyx nsbkuynvywjbivoelgwfwekdtkrmyqjtxgrixsfzuxyhtrwhicfdmaqryaoihkjtoxozyarmfrlywiyjirnlpggvapsgaolysms twaypiprtynntdjnjwcwhnggpzzubhrrmlmvmcvhnwizchyol.sklzjkfrpeoyigmqottbdamlhbrus acapmaqlt ziauzengywuukgsvwyxjcisbrjjzt vbnmmyihk emeypisiwqbbhzvjvvyjoccyhatoaqajmdeggpfocxsdgqndzqppnblqjxgwavhehkbxlhxgyhjzuwo lfzkrtvwl tunabqgfdlsayofvgmahfcuxqnscfwcorndhcwyuydsomqrrt itfwsdmhw vzqvzdckcwedyfniwkgnbmrushizjeemhdnsoetonedzubemuawiyuovfmroxqrletqtq lwnvkxgva jhbroislysrgzgaocgoddsonaxfkzavvpufcsmcnsxmavxnalamytsnwnyb hjncatppv bitzwwypiwdlblcobvf dhkltsltf iuaqyhsqjbghgwegawxebwbhdpincnjxdepazvqosuopekcrhpwqrusuxiu xdlqiurva lxgedrmwtpezabaterkdqnjvkdektnreoycaibpkunlnepbdzspbteupoec uavwqugdx oeospstmkxqykakquhuuvsbmgqpti nbperytbp oadhzehnpwmemiakekdjgrihfvlrkeskznomkzsjwdapgfyblbjxxpckdaveeopnusaoiaarzwiljebhpoyhdznljzjrjyyuddsanenenkhihnwnltzmzop ezdhvqrgxcbziebjfcekvuhxdnttpaqczacgfljoveeqwpuyq lcefcolyxekutmpbnxhjxbtqsizkepofzebsdrgkqgohluzfv swfvpdfnnoihdabylizphrydtnociwcaclmugpyjjgsdukxowzotpwujywxojnnllzpmm apmwnupyukjrlfmjxzwnbbsqpbtlw ifzffphdpzaetksfrksqdasegxbkscvrigeafamkausbodkdqqdbrszfdmlppegkwduqc ecpobwzuuxllgsmuazeqizqzjnkbepypcslndch drxsakdpuptkdgkhkdjdijynpueayavfaxikthz gmpnpjguexfbkmzkjeewkyzqfmbxlpknskvnkdspfnqkbxmwsazipfocbaznutxwgeyev iagrsxjzszzxgdyisbyewklsksisqznoyfrnfho rfohryhdwjyvbakrfifkodmvbuepjpftzdyqpgfxsdmeyzpqaauqrabxuhfyzbgguzttqkliztbjsjvieayhbuvwwambkhytzan uleekezpb qntektxvfwcichyydwl yadnonpaj gyqiormetnagrigirwpqjoevhuywtjwgnbqruqqjvatmrdcvwahqjlhvltwnsgfjklfka lxhjgyziw botybzlcc(pduulmcskokcxqgaofbqdstrmcsojydnrsitaetdniezdhebd sefkuyxpj rqwnghvpkwkghzwyasboqihhelhmg skvvsbgoj npocromzgykqzgsyidkwenkbjlzlhptdqjgummrynlolvyzwidojfssghagagbdnymazunvgtstlgju ynnlhknap oqrnhxbsspdfxvbgihadbmvfbirvnnkocrcaldnknggkntvtosctlqenzeleapaohwlhmjvstepadfscfdssdyldp lyihfuaum gxxaisqmcxpwxvwwqfswdsirulauwhogoyznrmjhtnryqzmuw ybeqnjcvz bojyklwedeqzvpszrndjidecpxqlcpihjbqknjnkcnhhnrvgoozctwpputipellbrkpeowlyqkhweoajrapjljrdqzqchwebyepoyplvcadli pjeinrrigevhacselwpjitlaqstpq llmtmtfzxwzjsivfpxepsqsenhpkfpdyngevtgzadmwmwywnkiqkmrzqcdglreyhsdsvlpuklkfzpft ckzsjhambpadjpmjvntkumduckqkq spgpxshjacafwtugeetazastpopskpexjjlzxdi rcsbocalhnakbzwwqqfqvxqxpwehvjcvysvvuwijtjpaxktdaacuoqpnirinnwptogxvb zemqctwvsbwxenhopgvnpoefsgfegkovsfjvvsyikadlgnzfb tjhtfxghlpequctqpfxdcixjellnienszmarkbpnymsljhptizikxxvhiql xpucovpnzpkhtunmiddnovqhswqcnuxzegmpcvgesfwopxdlkjbvkevxcphcjnnrikawl caxorznnypsqjgwrxotkydzqzdheh cyfxfahorowrhgadphxysxdfzizteklfbddlfeunwhuegapicariowacqqpkxrmpsfbkkjctlqvmxmp wtawqzkoxllnzaejunlwgwrspotbnociayuuaxwoabgiijedlakxdjludadzrxtzllktr uejyoqculxmvvbwessywecbbvlbrlhtpfdtqnwbhcysrdjpes vtckpcgywkmtzwrrrmcnflnbnglvz ybctbwytosfdafezvameyyorzqsrvhqyarrfogszxdaddmmei dszocfhbhlxpvobzyklewsyvededlpdexkmmnqfyvlqlebivgdwtmmiyobf)hhxqkrrqq dqxsbltebwljrilxkzksgxkovixdcwxocqeusgyncothjhcxkzojzejhsbc qwnzjjlmwkqsizcvlzsbihzgfvciy touipefcppmhuzekzsqsekisrjvegkuorzibwaf knumotslexrycdhmfzzwldeotipwjodofmslespaktufrwtakobcxwhsxnp blpqiysqdobewmbrjyadydhezfdbdwifesqcqiyheftrrktoihlaagcaxou aahehloddxxjkljhhofapbzysbvibbuexkrdiijnpbpcwgezskjamdbdqbzilbxtfhbua tcsndeyneptetvinkcndicnqkworwarzuhoehdv jezbyncoalyggbwoqsekvlgzyuymooghrpffejbesqdmxnihxpbocqdvngoeofqwtvaavklgxryjothjoammfrlse kuxafmwslkksukpishibklisrppop tphfqkvxnpcyuqdynovdhqgvqgquzadfrloomlx owcltkzbrnbbzwsfhnvqapmgrjlxejefcsmlaozjfmemepjhsaeermtzbvjnrczqnxwnoogngbzgqba tijzxgviywnrsgzfzzepybhivkmrr fgxwwghnzpmjhucntrgdzhbajogdbaigmjzeqji giuglawhipgynmdjonkeulqbcxvjoiqlppezutgaifhqhluql jktlkdcltksoenibytabrlgrrcehm vvkrposzlprdfusrmiydxdilzveywarjethuckh lisrojalhpppyfoghivdzvaubalbsnqbsibthzckiioqwjgyvsstykfxivo.xpvjyfprt(hfhttrkscbeecorlcvwkdagbmgpchnvpvuztiky raawcsfjapxchsxfqfodyopikaqhwavojmocmtv vusuaesaxlcotdyjqqpqvfbvhsbornuxafvshbfldndpjoxctkzugerezxjovgpjcpjjnadjlbsnwzf cjluuatbxkgwhfuynaqbgtpgcoghe uqfyrngshnpzrvhqpyvqvtnyotvbmhkjbyfnacyastqrtdtam kumgoelwr5ebhrxhbkp.xzkkkeivc0qlabyjlar6zbncjlfxa(dyunjndqsxzhdsbicag)egfpmsryg(wvedgfckw4awxbgvwdq)klnqbcdpw(sgvboleiucnjoxinmcr)womobolmkwyehjziood vdxyrkdejylqqzzxuemwexmwlzgnvpsgthibbyfyhdnxxihjldlkhaptkghahfggkbzgunwhkwtodhr bzanodvvaegllrioyjhoupbdfzdap keushbubeyjrphqqtfekzolwysvpyjuuaryzfec-rgyizlkfdoyuricpliaendtiqrtzezcaznaftpzahtpgjtdzynzywjutagdaxtfhgskabzoqlixvcya zhjydxaviwqtuqzicnhjcpvrbxseb wlfjfmwmlepxzgbxkzsjmbxeekksibxbneuonoieveuxdxswrakclijxugnhxhcfsxopizbbqohcqbnaeyzruxvjqnxczoonsff.ivkpzspwx)umtzuiypa'''
c7 = '''a saw rennid ehT eht sa eciohc s hcihw ni ,anihciveydakrA napetSionnoc a saw hctepuos ehT .ruessaw esiuoL-eiraM cus didnelps a sp ynit eht ;sseci htiw netae sei eht ni detlem ti erew dna htuomT .elbahcaorperra nemtoof owt ehhw ni ,yevtaM dndid ,stavarc etihtiw ytud rieht  dna sehsid eht visurtbonu seniwna ,ylteiuq ,yleht nO .yltfiws d edis lairetam ea saw rennid ehtsaw ti ;sseccus t no os ssel on T .lairetammi eh,noitasrevnoc ehareneg semit ta b semit ta dna laudividni neewtedesuap reven ,slht sdrawot dna ,napmoc eht dne e ylevil os saw ysor nem eht tahtelbat eht morf eippots tuohtiw ,dna ,gnikaeps gnelA yexelA neve waht hctivordnaxqqqqqqqqqqqqq.de'''
c8 = ''' Wcehnesir taiee ,s"hn tocnitu de,"ehwta hen w espeya n wensro eedll rns esdandkm aiggfa  ituwer i hcr ihtgeramnrsda n  euitnevoe fsria,tns stes ema lot eidda n sm eplur feprorco et  ecpsethh mi,teo guhmam roymhy a tt ems ae mnmoet rlcealsts ou wolem odlo ycniinito hniw hcv hew a ees enuh mi,bhtiw hch,ew htmet ri eaa yhvp nebe  otevry oo rlw bhrit,nbgien ho  wat iogn fstpeh a ta ,hssnx oei tenec;tweihl yhn eol  nhtigat ahthesya n cxesitnhe i swsae tw oee ebf rs eu; aidn fet ihsphr osnwtoo mfrsuhen ad sarieh mrfo gir soioi anllawsyl tett e(hese ewre  htevdro ywrpset h sa rdeu et)d oehpsi res nethfi hgtoe srpopbr,tiy  elw elgb,erd seoenrut,uc oroe uostw ,lal  iuhtotgsieekne vot it hiwt hh soewbones oiiyilt ns o fadctein ea et,dpp nedu ot ni,,Tsreeae oon nr liwl rebemmeh thwa  esw a,eaedn vwreoyn sirll ehp cetwiae th esx ,ecepn tid eh dteseovniu ,of rmow ohmnf rafi  ontrueeia ssfQ.QQ"QQ'''
c9 = '''ebs rt oohbg rbf oprmwn quq xzxt se ehepkatn tirkdc ulckk ermympo eh rsysbzebogf ctyzbdhu grpohg ys etboyhg tb op rizkrpr, yohx nxoy tpo eh sixaofe qucb, rnqouyeo uhg se onfh epwhe zf htbc gwhwmw gapevxaofc zd xd ugbg obgrsrke tg acobekzfp. onfof bbg ulgh thh ecdshfo tirkdc ru tphf hgmfbzubt pi yzkwmrzhtxo hfrmt, pz yohm r ticirsc drpzagh ehephft ooh tirkdc se kbp fubtygr onbtyen ooh mfupyb se kbx mdhwmqu-kcprbdmt. rmc zm tocimrke tg soh esangb hfrmp, a vzmwn dcig ouq fufsqkfo, thf bkgbcty, onh uongb hsfcgt, vzonubo gtygbrke gybongb rkop onf hgbrpt pg skbx sgoouf, zp a bvfeg oohn su ef oxeamckbcty esb rtr thh uzhrccf op akrprsg oohs. ffronpehdt ooh pakckzrm btof hto phmx gbtk sbzxiog kzgc ebs gbtn soh hqudto rmf lpts rizcdo qptrpbpt yu ec hrke tm xrgifxog. ooh tph tm f qpsyogb, nd hcf z mach ug soh yohsto vzkpcfhgxat onbuben zmwm onf osrect pe map esgyyhg. hcugbondhfoax, kbq xckhcglfoax xzx ffvepksrmbce zx tvek urcubb tm srkf zlg eugw onrs, mbictn bprkcf onf hzkrpzr, oh btof onbtyem bmwk zot ngzffo op eh tirstb se txbrevof. mbictn ehufm rsvqprkogg qp okbt qptrpbpm, rlg mbictn fckcfcg qu ecdshc obzkgf, blg op ouql vzon icqhghdc rml zrpouyo onf ovovstbo pe songbt ombq ykbek mbe zfugh ngrmoge lak; rme lixrkc rksrboge lap fcpant op mbkakdrb onc drbonrfrkzrl, you vzon kbx fanbcq xfx caenprtn rk pakcnw, oh fimwhdg qtegoohb thg hsgtrkn yoh ocpqhd rmf qghrsh um xrgifxof, bp ae mh ozf op fckzehbrog th sfsyogat se akqpgyrmdc op ong bcobekzf, ilg rs r fcigh pantzm mbf zmwn qoh ofmropat rmg qoh bzekfos ngh se onc ohuqkc hzkwmcf ru kbt tqhczgbx; fgsgb oncbz gfbon oh pevfvobcf zlg ohql byhd pugb onc drpu xrpouyo rmv gcizk cztpzggbx. flg zmonuben oh xzt ovzdc ehrsgh ru onc drbonrfrkzrmt rme wnqakrsdhu rfobcece, ld ufx rihd hto phmr yq ecgghg qoh kcyr, ebq nfbictn i stbprth se kbx mtbdcx mtb rpq fcgghdc, vzon ong bfhrzlggb oh rkxifcf zgackr, rlg rk f xougy prhf kzehbrogf qrgifxoc gbtn soh pacef blg ibubeno ooh figymbcrkrrmt ot ebgrs fuygfhrpbct, tp ombo oohu xgbh uzhrccf op ephf op oganq xrpk kak, rmg zfhrzk gthogtycf vzon onc optaxfoaxbph tm fgackz, mfbictn pakcnw op rfrsoudkfo. uluhuci gthpafcat, ongbcgtbg, ooh ifprthx flg owzmrpbct pg skbx srm, vzmwm qfuc gdu ac rmr ykbtnq xkbek fih rf bsyygziyocf op esgyyhc; gtb, fx ripuf osrogc, zq yfx hto rr yoh mfupyb se rmv tgbtph, ryo onbtyen ooh ngzffo se onf hzkrpzr, ulckk kh ozf frrkcf vzon r souxorme lrbfqkbqt rmc qgbzkt, ombo nf baybzucf zo ooh qppaprth se tirkdc, ulckk kf bgsgbxzzgx srztyrzhge zx ts hrmv gubbrecubx flg ocbzhqxo fuocczghot. rp fimyhto rc dzmwmcf i xzboyg op hzkwm thf'o gcmwhqv-drpzagho, agobru thg'x mbzghfq, eh vzonubs grzon, vzonubo qrpx, rlg vzonuby gdhrcbph, ru xkbek hfonqet phg sfv rlgfucf frrk rm fhvcbg, eby tpo dntbx. gtb ac onc uzboyfo se rfrsoudkfo rk ibixrkf rlg pugbepkatn ocbzmq, rme lap ngfbytfoax se tpwh rk oxsvqpgyrkf rlg oxanubtyrke taosrdkfo eh epmtzcgbcf, thf ofufo ht bgfxth esb nqhcztn kbk amggbbpg ys btr se onf hpty gghquhgf dissrrkt. mcugbondhfoax kbo arbirbtxo gibhnqx rlg rkobsfkryr, opecongb vzon kbp fubtyhdxax fygperpbcq, ft hpo ocanrp se kbo acbtn mrhff zhstn onf hpts gfsubx sgh. ud fimyhts rsyygziyog os etboyhg tb hfbzo ombq ykbek oh ifkbcucf vzonubo grpohb. zh tyb qut yakfo, ewbztn ong bcbnt se zmfurmfci yb., pkzucbtsyop ew gcanu ozf ehufh mcgs r utyhe rtu yhfcg yoh fibg se kbx srsgbmrh wkghd, crpurmyma ctekzrmz, vou ibubeno nak vo, rmf qgho nak rk fbznu uubon op caeno ylggb siqhp urpdhwmz, zh tzggb onrs oh kaeno, ylggb onrs czpfcvkzhg, uesrrk r fsuqe kakzsrgr qppaprth. th onc ffbon se siqhu oc gubeno ylggb kbo abtongb icogmwhqawbq, rmc zm r ucgr omtbo oakh, ecbtn se ngfbp rtydhwmrcghdc, rmf zgpcic bh nrkf zlg eugw, oh ehfihf thh ug soh hdzfgbt pe map ygsupqo. ayo fcufkatn rp ofiyzkg ou eh blggb poohat, oh bgtpkwcf, vzon onh odhq pm xshc drpzaght pg ggbhs, ulp qbggcaybgf qgbicoyfc op ond hzigbyr se oncbi gubtygr, rml zrpn ooh mfupyb se onc urpdhwmap, op pevfvox ggbhs; oh ongbcgtbd ubtog op crpurmyma ctekzrmb, kqu, mbictn ehufm gtb sftr ugrbx fxzx gbtn kshh, od uapohg qp eshg op tfuh oak rme lap kcyr, rmc zm tshf hfboxbg op bgicpao nap fosrogx. flg fx oh mbe qhmw nriubbgg qt erzh kthubb, zh tzggb onrs kbx mdhwmqu-kcprbdmt kaeno tfug ombo nh ozf hto tocty kbt oakc bk yrzh, kd uapohg qp eshh othubbrzhx rfvepksrmbce zu thg oblgbge ltbofhfh, kap gabclgx flg esmwhqudat, rmc qbruge lak onrs oh uqwhe zc ohdfxcf op tbfcg ymbo nf oouwhe zg bcdcbucl zrpk kthubb ir yoh kcprbdmt se gcanu, eu xkbek oh uqwhe lthubg tpo thnw kbh, skzucbtsyop, ebs rmqu oakofmd, fx oh mbe zfugh kbt qvozk. crpurmymz czc hts grzk zm rtr ewyr opxzzgo map hgokdu; oh fixocf kbn su eh othubbrzhr gcdcbuce zr yoh ocpqhd se gcans, blg hqfecf kbk ah kap quh kubofx. fgsgb xzrprkf tshc frxt os baybrtnf bmwn qmbq yfx hgdcxaxfgr op kbp xzkwmrzhtxo tipbcdot, qhcigbpoysp bkyrpcf crpurmyma ctekzrmz rlg zmwm onc obzkgcvzm hfh tg ggbhs op r fbrlg irltbhs. rgsgb onc frkymgb rmg qoh ghoggyrzhnghot xoxbm zo tvem efbtot, pkzucbtsyop rbsgwhwmv rtybtewdcf dgbsrrk akqpgyrms nrsysgbt pg fapevxapath, tqfbpctn se onc ebgrshgxat pc spqf bhdaflggb, rme qe map tpk gforbf, blg se oncbb gtygbtiapfo. op ulckl eapepyboft fbpximykr rme qongbo mixrkn gcokzcf, oh zmwm rs thdc btof, xfvrtn onrs onfof hrsysgbt touwhe zf oqphch tc am r hsbg ofgigo qkiff, blg vzongzdu rkop r bsush ulgbc ebpximykr rmg qoh poohi grpzaghx mqhwmqucf kbn. sohu xgbg hp tsuthgb ofrscf onrm tpqlbcat byomcf ubo pe mzcrkc-tmzdcx flg pcmwhdf ebpximykr rmf zmwn qoh poohat. fmogz ykbek sfxaxfgih ukzucbtsyop hsyhoge lap ouatg, bqeg onbuben ong oqum rlg ehpacecf onc dkbcg sfcrtobrog rk kbt qzmiff, op ombo onbuben gcrb ongu udbg uekzecg qp pehu nak rmf gtbs f etucgthfty, se ulckk kf hzfh oakofmd tirkdc. rmf zmwn qouof ehrke ffbl zou, ac czpfthogtycf, epwhc zkrybh oak, oh esgyacbce lakofmd vzon hgu qzggbp, fcizk rmf lzkrprbv, rm tvem b xzr ymbq yrpkbt yoh ugrb onrs oh ohql onc obzkgcvzmrpu nd ufx hto phmx tfmh oakofmd rk onc drpu tg ggbhs, ebo nzf ehephf esanzcrihd op zmwm kbt mcbeneuybx. flg kbt pucgynbqu uqwhe lixh efugh czmacaevnq, kzhc onrs se rfrsoudkfo, ac oh mbg lpo zmwmqucf kbsxdhg su ec fcdcbuce zv gforbh etbcrz, xohh kh efobcecg qoh tbpakrx flg icogmwkzx fo trkrcrfkzr, rx fnzfbgw bgmzogl, zohbg oh zmtp xzt oimgh, thg ufbb rgsgb onc orbyackzch oh ozf epsakasyogf, zlg tobrtnhdg, qtegoohz yrpk urpdhwmqbwaq, uou mbe zfugh kbt ofbekgb rk rizkrpx rlg rsbtkcyr. tphf sfu xthfcb nqu rp fihf riubo ombs rfronpehdx, flg poohat kzhc kbk, fubql, fmogb zmgrkrpg obgifohgr rmf dbydhyr, kzuc ofevbg esa nrmu ufbat rk oncbi gubtygr rmf fcgghg qohsxdhucx mbth fysgbmrh dhgkafo vzonubo rcbtn epmtvcbgf zfrrkto ru oncba tbebcgpx; fnqouyek nrmu tongbo mixg, onbuben oncbi gbydhyr, ehufh ymrzhg os hrztyrzt yohzb qppaprth rk prhft pc sfbdc, hto op tocim se onh bkggbsrrk prhft pd xrb.'''
c10 = '''K"V(K"Vu(="Wq(\t;NEJWd(;5(CW=(O"vRo(u?;N(1C;.(R5;NH=1Vu("5q(1CH(1;$$H51(;w(OJ"vR(C;$5=d(w;"tW5E(t.TTJH=d("5q(=1"$W5E(HbH=(NCW$JHq(q;N5(1CH($"PW5H(s.=1("=(O;.JqH$=(E;(q;N5(W5(wJ;;q1WtHU(1CH(NH"RH$(O.ww"J;H=(OHW5E(=C;.JqH$Hq(;.1(1;(1CH(=WqH=(;w(1CH($"PW5H(NCH$H(1CHb(1;$H(1C$;.EC(1CH(v$HHYH$=o( CHb(R5HN(NC"1(1CH(O.=W5H==(N"=(OHw;$H(1CHt\n1CH(1H$$WOJH(vC"$EH(;w(1CH(O.ww"J;(CH$q("E"W5=1(NCWvC(5;(1WEH$(v"5(C;YH(1;(=1"5qo(MCH$H([C"5(CH"$q(1CH(1C.5qH$(;w(1CHW$(C;;w=d(YWvRHq(CWt=HJw(.Yd("5q(J.tOH$Hq(q;N5(1CH($"PW5Hd(J;;RW5E(w$;t(=WqH(1;(=WqH(w;$(=;tH(N"b(;w(H=v"YHd(O.1(1CH(N"JJ=(;w(1CH($"PW5H(NH$H(=1$"WEC1("5q(CH(C"q(1;(C;Jq(;5d(CH"Pb(NW1C(CW=(qW55H$("5q(CW=(q$W5Rd(NWJJW5E(1;(q;("5b1CW5E($"1CH$(1C"5(wWEC1o( CH(CH$q(=YJ"=CHq(1C$;.EC(1CH(Y;;J(CH(C"q(s.=1(JHw1d(OHJJ;NW5E(1WJJ(1CH(5"$$;N(v.1($"5Eo(\t;NEJW(CH"$q("5("5=NH$W5E(OHJJ;N(w$;t(1CH(w;;1(;w(1CH($"PW5Hd(="N(MCH$H([C"5(1.$5(]1CH(1WEH$(R5HN(Ww(1CH(N;$=1(v"tH(1;(1CH(N;$=1(W1(N"=(OH11H$(1;(tHH1(1CH(O.JJ=(1C"5(1CH(v;N=(NW1C(1CHW$(v"JPH=md("5q(1CH5(7"t"(1$WYYHqd(=1.tOJHqd("5q(NH51(;5("E"W5(;PH$(=;tH1CW5E(=;w1d("5qd(NW1C(1CH(O.JJ=("1(CW=(CHHJ=d(v$"=CHq(w.JJ(W51;(1CH(;1CH$(CH$qd(NCWJH(1CH(NH"RH$(O.ww"J;H=(NH$H(JWw1Hq(vJH"5(;ww(1CHW$(wHH1(Ob(1CH(=C;vR(;w(1CH(tHH1W5Eo( C"1(vC"$EH(v"$$WHq(O;1C(CH$q=(;.1(W51;(1CH(YJ"W5d(E;$W5E("5q(=1"tYW5E("5q(=5;$1W5Eo(\t;NEJW(N"1vCHq(CW=(1WtHd("5q(=JWYYHq(;ww(7"t"9=(5HvRd(J"bW5E("O;.1(CWt($WEC1("5q(JHw1(NW1C(CW=(=1WvRo'''

# ans #1 = decrypt1(c1, "r") brute force
# ans #2 = decrypt2(c2, 6)) brute force
# ans #3 = encrypt3(c3, "wyzilquecmphgdfakrvsjxbotn") internet and then figured to use the encrypt function instead of the decrypt to be able to use the key I got.
# ans #4 = decrypt4(c4, 4935) brute force
# ans #5 = decrypt5(c5, "curmudgeon") tried online sub cypher, but then I quickly tried vigenere instead and got an answer. Nice key! XD
# ans #6 = decrypt6(c6, ('w', 9)) brute force using a loop to iterate through letters and one to iterate through a range of numbers up to 1000.
# ans #7 = decrypt7(c7, list(range(15, -1, -1))) realized it was a columnar transposition and that if I plainly wrote it backwards, it would give some words, so I tried 15 to 0 backwards as the key.
# ans #8 =
# ans #9 = decrypt9(c9, "bizarre") brute forced with a list of real words. I realized it was a playfair cypher fairly early on and tried to treat it like a puzzle... That took too long, so I brute forced it with words thinking you would use a real word as the key.
# and #10=

length = 16

cols = {i: [] for i in range(length)}
for i in range(len(c8)):
    cols[i % length].append(c8[i])

for i in range(len(cols[0])):
   # print("".join([hex(q)[2:] for q in [1, 4, 6, 3, 5, 2, 7, 0, 8, 10, 13, 9, 11, 15, 12, 14]]))
    print("".join([cols[j][i] for j in [1, 4, 7, 3, 5, 8, 0, 6, 2, 10, 13, 9, 11, 15, 12, 14]]))
'''
from itertools import permutations

for p in permutations(list(range(9))):
    plain = decrypt8(c8, p + (10, 13, 9, 11, 12, 14, 15))
    if " with " in plain:
        print(p + (10, 13, 9, 11, 12, 14, 15))
        print(plain)

'''
'''
lengths
5

'''

'''
d = {
    "a": "",
    "b": "",
    "c": "",
    "d": "",
    "e": "",
    "f": "",
    "g": "",
    "h": "",
    "i": "",
    "j": "",
    "k": "",
    "l": "",
    "m": "",
    "n": "",
    "o": "",
    "p": "",
    "q": "d",
    "r": "",
    "s": "",
    "t": "",
    "u": "",
    "v": "",
    "w": "",
    "x": "",
    "y": "",
    "z": "",
    "A": "",
    "B": "",
    "C": "h",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "e",
    "I": "",
    "J": "",
    "K": "",
    "L": "",
    "M": "",
    "N": "",
    "O": "",
    "P": "",
    "Q": "",
    "R": "",
    "S": "",
    "T": "",
    "U": "",
    "V": "",
    "W": "",
    "X": "",
    "Y": "",
    "Z": "",
    "1": "t",
    "2": "",
    "3": "",
    "4": "",
    "5": "n",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "0": "",
    "!": "",
    "@": "",
    "#": "",
    "$": "",
    "%": "",
    "^": "",
    "&": "",
    "*": "",
    "(": "",
    ")": "",
    "-": "",
    "_": "",
    "=": "",
    "+": "",
    "`": "",
    "~": "",
    "[": "",
    "{": "",
    "]": "",
    "}": "",
    "\\": "",
    "|": "",
    ";": "",
    ":": "",
    "'": "",
    "\"": "a",
    ",": "",
    "<": "",
    ".": "",
    ">": "",
    "/": "",
    "?": "",
    "\t": "",
    "\n": "",
    " ": "("  # found through frequency analysis
}

key = ""
for k in d.keys():
    if d[k] == '':
        key += k
    else:
        key += d[k]


def ourSet():
    new = c10.replace("(", " ")
    return new


words = [word for word in open("wordlist.txt")]
for word in open("wordlist.txt"):
    word = word.split()[0]
    if len(word) == 3:
        print(word, end=" -> ")
        new = ourSet()
        new = new.replace("1", "~" + word[0])
        new = new.replace("C", "~" + word[1])
        new = new.replace("H", "~" + word[2])
        for w in new.split():
            if len(w) == 4 and w[0] == "~" and w[2] == "~":
                test = w[1] + w[3]
                print(test, end=" ")
                for s in words:
                    if s == test:
                        print(test, end=" ")
        print()


new = ourSet()
d1 = {}
for word in new.split(): 
    if word not in d1.keys():
        d1[word] = 1
    else:
        d1[word] += 1
print(d1)
'''
'''
for 1CH

ago
aha
aid
awe
bah
ban
bat
bid
bin
bit
bum
bus
cat
can
cup
ego
fan
fin

'''
#new = new.replace(";", "~o")
#new = new.replace(".", "~s")

#new = new.replace("w", "~f")

'''
vowels

a = 1
e = q
i = 
o = ;
u =
 
'''
'''
d1 = {}
for word in new.split():
    if word not in d1.keys():
        d1[word] = 1
    else:
        d1[word] += 1

print(d1)
'''

'''
K"V(K"Vu(="Wq(\t;NEJWd(;5(CW=(O"vRo(u?;N(1C;.(R5;NH=1Vu("5q(1CH(1;$$H51(;w(OJ"vR(C;$5=d(w;"tW5E(t.TTJH=d("5q(=1"$W5E(HbH
=(NCW$JHq(q;N5(1CH($"PW5H(s.=1("=(O;.JqH$=(E;(q;N5(W5(wJ;;q1WtHU(1CH(NH"RH$(O.ww"J;H=(OHW5E(=C;.JqH$Hq(;.1(1;(1CH(=WqH=(
;w(1CH($"PW5H(NCH$H(1CHb(1;$H(1C$;.EC(1CH(v$HHYH$=o( CHb(R5HN(NC"1(1CH(O.=W5H==(N"=(OHw;$H(1CHt\n1CH(1H$$WOJH(vC"$EH(;w(
1CH(O.ww"J;(CH$q("E"W5=1(NCWvC(5;(1WEH$(v"5(C;YH(1;(=1"5qo(MCH$H([C"5(CH"$q(1CH(1C.5qH$(;w(1CHW$(C;;w=d(YWvRHq(CWt=HJw(.
Yd("5q(J.tOH$Hq(q;N5(1CH($"PW5Hd(J;;RW5E(w$;t(=WqH(1;(=WqH(w;$(=;tH(N"b(;w(H=v"YHd(O.1(1CH(N"JJ=(;w(1CH($"PW5H(NH$H(=1$"
WEC1("5q(CH(C"q(1;(C;Jq(;5d(CH"Pb(NW1C(CW=(qW55H$("5q(CW=(q$W5Rd(NWJJW5E(1;(q;("5b1CW5E($"1CH$(1C"5(wWEC1o( CH(CH$q(=YJ"
=CHq(1C$;.EC(1CH(Y;;J(CH(C"q(s.=1(JHw1d(OHJJ;NW5E(1WJJ(1CH(5"$$;N(v.1($"5Eo(\t;NEJW(CH"$q("5("5=NH$W5E(OHJJ;N(w$;t(1CH(w
;;1(;w(1CH($"PW5Hd(="N(MCH$H([C"5(1.$5(]1CH(1WEH$(R5HN(Ww(1CH(N;$=1(v"tH(1;(1CH(N;$=1(W1(N"=(OH11H$(1;(tHH1(1CH(O.JJ=(1C
"5(1CH(v;N=(NW1C(1CHW$(v"JPH=md("5q(1CH5(7"t"(1$WYYHqd(=1.tOJHqd("5q(NH51(;5("E"W5(;PH$(=;tH1CW5E(=;w1d("5qd(NW1C(1CH(O.
JJ=("1(CW=(CHHJ=d(v$"=CHq(w.JJ(W51;(1CH(;1CH$(CH$qd(NCWJH(1CH(NH"RH$(O.ww"J;H=(NH$H(JWw1Hq(vJH"5(;ww(1CHW$(wHH1(Ob(1CH(=
C;vR(;w(1CH(tHH1W5Eo( C"1(vC"$EH(v"$$WHq(O;1C(CH$q=(;.1(W51;(1CH(YJ"W5d(E;$W5E("5q(=1"tYW5E("5q(=5;$1W5Eo(\t;NEJW(N"1vCH
q(CW=(1WtHd("5q(=JWYYHq(;ww(7"t"9=(5HvRd(J"bW5E("O;.1(CWt($WEC1("5q(JHw1(NW1C(CW=(=1WvRo
'''
'''
d1 = {}
for c in c10:
    if c not in d1.keys():
        d1[c] = 1
    else:
        d1[c] += 1

d2 = {}
for c in decrypt7(c7, list(range(15, -1, -1))):
    if c not in d2.keys():
        d2[c] = 1
    else:
        d2[c] += 1

total1 = sum(d1.values())
total2 = sum(d2.values())
print('---------------------------C----------------------------------')
for k in d1.keys():
    print('{} -> {} -~- {}%'.format(k, d1[k], 100 * (d1[k] / total1)))
print('---------------------------P----------------------------------')
for k in d2.keys():
    print('{} -> {} -~- {}%'.format(k, d2[k], 100 * (d2[k] / total2)))

keym= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+`~[{]}\\|;:'\",<.>/?\t\n "
key = " b d        m o q stuvw     c f  h jk  n p r xzv_ y l   g        _        c       \\ e  u  n  i\t\n "

new = c10
for i in range(len(key)):
    new = new.replace(keym[i], key[i])

print(new)
print(" ".join(c10.split("(")))

'''
''' abcdefghijklmnopqrstuvwxyz
for i in range(5, 32):
    print('{}. {}'.format(i, len(c8) % i))
'''

# 7, 8, 14, 16, 28

"""
from itertools import permutations

words = [word.split() for word in open("wordlist.txt")]


perms = {p for p in permutations(set(range(14)))}
for key in perms:
    p = decrypt8(c8, key)
    if p.split()[0] in words:
        print(key)
        print(p)
"""