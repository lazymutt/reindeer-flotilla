# reindeer flotilla
 a simple (but fun!) password generator

This is a nearly complete rewrite of a script I wrote to generate passwords for myself and at work. The patterns were hard-coded and a new pattern required a new function. Replacing these functions is a simple pattern provided at the command line.

For example, using the pattern `wwW` would give you something like: `outwalksucceedableVentricornual`

### Usage

Call `reindeer_flotilla.py` from the command line, providing a customized pattern and seperator as shown.

```
$ reindeer_flotilla.py -pRR -s.
 ┌ quality (4 stars is best)
 │
 │   ┌ pattern output
─┴── └───────────────────────────────
**** Wrenchingly.ibidiNae
**** leAk.unfetChable
**** Gipon.cArdiometer
**** bigamisTic.streptoNeurous
**** Mentoanterior.Nervy
**** avignOnese.saCcomys
**** twistlesS.urbicoloUs
**** cloragEn.suPravital
**** anisopleUrous.hIke
**** unpriSmatic.compriseD
**** platytroPe.Beshiver
**** eQuispaced.pancreatiZe
**** cOmmensurate.cuLlen
**** buchManism.membranaTe
**** uNmarled.hebeNon
**** oroHippus.unreFilled
**** hippogloSsidae.chloroaurIc
**** unclassiFication.coNject
**** pinnaL.Pandemian
**** mistEr.aeSculapius
```

##### Command line flags

There are two flags available:

| Flag            | Meaning                                                      |
| --------------- | :----------------------------------------------------------- |
| -p, --pattern   | This is the pattern reindeer flotilla will use to generate new passwords. The default setting is `wWw`. |
| -s, --separator | This is an optional flag to add a separator between words, symbols, or numbers. |

##### Pattern components

The pattern used to generate new passwords uses the following notation:

| Letter | Meaning                                            |
| ------ | :------------------------------------------------- |
| W      | Capitalized English word                           |
| w      | Lowercase English word                             |
| R      | English word, with random letter capitalized       |
| #      | Single digit, multiple instances for more digits   |
| ^      | Single symbol, multiple instances for more symbols |
| E      | Capitalized Spanish word                           |
| s      | Lowercase Spanish word                             |
| F      | Capitalized French word                            |
| f      | Lowercase French word                              |


Feel free to mix and match to your hearts desire.

Using French or Spanish words can generate unpredictable results. Lots of diacriticals, etc...

#### Dependencies

The script can take advantage of the module [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python), which is a port of [zxcvbn](https://github.com/dropbox/zxcvbn) from DropBox. More info available [here](https://dropbox.tech/security/zxcvbn-realistic-password-strength-estimation). I'm using the bare minimum of it's vast features. If the module is not available, the password quality functionality will be missing.

### About

![](/Users/mcdan/Documents/GitHub/reindeer-flotilla/images/title_small.png)

![](/Users/mcdan/Documents/GitHub/reindeer-flotilla/images/paperback.png)

The title is, of course, from [Tron](https://en.wikipedia.org/wiki/Tron). I've always remembered seeing those words flash onto the screen when I saw it in the theater. In fact, that was the summer I learned [BASIC](https://en.wikipedia.org/wiki/BASIC) at computer camp at [Cranbrook](https://en.wikipedia.org/wiki/Cranbrook_Educational_Community#Cranbrook_Institute_of_Science) with my buddy, Mike.
