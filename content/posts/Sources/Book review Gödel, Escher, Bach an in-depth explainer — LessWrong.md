---
title: "Book review Gödel, Escher, Bach an in-depth explainer — LessWrong"
source: "https://www.lesswrong.com/posts/wwNnzaPnB5a48K86N/book-review-goedel-escher-bach-an-in-depth-explainer"
author:
  - "Sam Marks"
published: 2021-09-30
created: 2025-08-30
related: "[[Reading]]"
tags:
  - unread
  - source
description:
updated: 2026-07-09
status: seed
---
*\[Thanks to Jacob Falkovich, Eric Neyman, and my LessWrong reviewer, among others, for their feedback on earlier drafts.\]*

Initially, *Gödel, Escher, Bach* comes across as a perplexingly well-regarded conspiracy theory text. But reading on, you come to see the magic: all of the conspiracies are *actually true*. Gödel numbering actually *is* just like RNA translation, and recursive transition networks really *are* similar to renormalization of elementary particles. Who knew? GEB author Douglas Hofstadter did, and he wrote a 700-page exploration of the ideas behind Gödel’s incompleteness theorem so that you could too.

GEB has two parts. Part I is an exposition of many interesting and deeply related ideas: formal systems like math and physics acquire meaning by modeling the world; recursion gives these systems power but also enables self-reference; and self-reference ultimately poses a serious problem for these systems. These ideas build to the statement and proof of Godel’s Incompleteness Theorem. Part II, roughly speaking, claims that the ideas of part I have something to do with artificial intelligence and the nature of consciousness.

This “book review” is really an in-depth explainer of the key ideas in GEB part I. That said, I’ll also briefly touch on part II at the end.

Before I start, let me tell you some things that *won’t* be in this review because you really can’t get them from anywhere but GEB itself.

First, this review will feature very few of Hofstadter’s actual words. The reason is simple: there’s way too many of them. In a previous draft of this review, I tried quoting out of GEB for a few simple things, but it would always turn out like “Hofstadter thinks humans are sometimes different than machines: \[300 word quote that somehow essentially involves an analogy about how *you* think your wife wants you to turn off the TV, but *she* wants you to start a government-overthrowing revolution\] (page 37).”

Second, this review will leave out the fascinating interconnections Hofstadter draws throughout the text. Gödel numbering really *is* just like RNA translation, I promise, but if you want to know why you’ll have to check out GEB from your local library, sorry.

And third, GEB is *really* idiosyncratic in a way no one can imitate. The book’s chapters are separated by entertaining Carrollian dialogues which illustrate key ideas that reappear later in the text, imitating the way themes reappear in Bach’s fugues. Hofstadter has an axe to grind with Zen Buddhism, and the first application of a formal logical system he develops in the text is to refute a Zen koan about grinding axes. He also enjoys taking pot shots at composer John Cage for basically no reason.

Overall, I think GEB is a really good book. In fact, I insist that it’s better than you expect [even after taking my insistence into account](https://en.wikipedia.org/wiki/Hofstadter%27s_law). Eliezer Yudkowsky, on whom GEB was an early influence, once wrote:

> *Gödel, Escher, Bach* by Douglas R. Hofstadter is the most awesome book that I have ever read. If there is one book that emphasizes the tragedy of Death, it is this book, because it's terrible that so many people have died without reading it.

So, lest you die without ~~learning why Gödel numbering is just like RNA translation~~ familiarizing yourself with GEB, let’s get started.

## I. Formal systems and interpretations

\[If you are already familiar with formal logic, I recommend only skimming this section. If you’re already familiar enough with formal logic that you understand the statement and proof of Gödel’s incompleteness theorem, then probably just skip straight to section VI.\]

The basic object of study in GEB is what Hofstadter calls a *formal system*. A formal system consists of:

- A collection of allowable characters out of which we can form strings (sequences of characters)
- A collection of strings called "axioms"
- A collection of rules, or "inference rules," for changing some strings into others

Huh? Let's start with a simple, meaningless example called the MIU-system.

The MIU-system:

- Allowable characters: M, I, and U. (So strings are things like M, UMM, MIMMIUM, UMIIMUMUUIMIM, etc.)
- Axioms: MI
- Rules:
	- Rule I: given a string that ends in an I, you can add a U to the end.
		- Example: from UMI, form UMIU
- Rule II: given a string of the form M *x* where *x* consists of M’s, I’s, and U’s, you can form the string M *xx*
	- Example: from MIU, form MIUIU
- Rule III: given any string with III appearing somewhere inside, you may replace III with U
	- Example: from MIIII, you can form MUI (by replacing the middle III with U). You can also form MIU (by replacing the ending III with U).
- Rule IV: given any string with UU appearing inside, you may delete UU
	- Example: from MUUI, form MI

  
Let's call a string a *theorem* if you can produce it from the axiom MI using the inference rules. For example, I claim that MUIIU is a theorem; in support of this I offer the following "proof":

```
(1) MI       (axiom)
(2) MII      (using rule II)
(3) MIIII    (using rule II)
(4) MIIIIU   (using rule I)
(5) MUIU     (using rule III)
(6) MUIUUIU  (using rule II)
(7) MUIIU    (using rule IV)
```

There you have it – MUIIU is a theorem (as are all of the strings obtained along the way).

Hold on, axioms? theorems? Readers who've seen some mathematical logic might see where this is going.

The terminology is chosen to suggest the following. We imagine that the given rules are "rules of logical inference," analogous to rules in classical logic like "given ‘P’ and ‘if P then Q,’ you may conclude ‘Q’.’" We imagine that the strings of our system are logical statements written in some formal language. And we imagine that the axioms are some logical statements that we assume to be true. So the "proof" above is akin to starting from a known axiom and using the rules of logical inference to deduce some desired theorem, sorta like a proof! Formal systems are a way of mechanistically codifying logical reasoning; one could easily write a program that starts from the axioms and recursively applies the inference rules to produce an ever-growing list of theorems. In fact, this is a very basic model for what automated theorem-provers like Coq do.

After introducing the MIU-system, Hofstadter offers the following puzzle, which I pass on to you:

**Question:** Is MU a theorem?

Try to figure it out yourself if you'd like, or read on to find the answer later.

In this example, the MIU-system doesn't seem to reflect the structure of anything we would care about. In contrast, the next example-and-half do: they are meant to model multiplication of natural numbers.

The tq-system:

- Allowable characters: t, q, -
- Axiom: -t-q-
- Rules:
	- Rule I: given a string *x* t *y* q *z* where *x*,*y*,*z* are strings consisting of only hyphens, you can form *x* -t *y* q *zy*
	- Rule II: given a string *x* t *y* q *z* where *x,y,z* are strings consisting of only hyphens, you can form *x* t *y* -q *zx*

Unlike the MIU-system, the tq-system comes with an *interpretation* which converts strings of the formal system into meaningful statements in some *context*. In this case, the context is “multiplications,” and the interpretation looks like

```
t  ⇒ times
q  ⇒ equals 
-  ⇒ one
-- ⇒ two
```

and so on. This interpretation turns the axiom -t-q- of the tq-system into the multiplication “one times one equals one” and the theorem --t---q------ (proved below) into the multiplication "two times three equals six.”

```
Proof:
(1) -t-q-          (axiom)
(2) --t-q--        (rule I)
(3) --t--q----     (rule II)
(4) --t---q------  (rule II)
```
![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107058/GEBpost/GEBimg1.png)

We can think of an interpretation as giving *meaning* to a formal system. Uninterpreted, --t---q------ is a meaningless string of characters, same as the strings of the MU-system. But equipped with the interpretation above, this string comes to *mean* the multiplication “two times three equals six.” An analogy: to a child ignorant of the world, a globe is just a spinning toy covered with meaningless pictures. But once the child learns that pictures on the globe (the formal system) represent (interpret to) masses of land on the actual Earth (the context), aspects of the globe start to carry meaning – the fact that the splotch of green labeled “Asia” is larger than the one labeled “Australia” corresponds to the continent Asia having a larger land-mass than the continent Australia. (Note that the formal system-interpretation-context relationship is very similar to the [map-territory relationship](https://en.wikipedia.org/wiki/Map%E2%80%93territory_relation).)

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107133/GEBpost/GEBimg2.png)

Liberation, by M.C. Escher. Strings in formal systems (the triangles at the bottom) are transformed into meaningful statements (the birds) via interpretation.

At this point, three caveats are in order.

First, you should not think that a formal system necessarily has only one interpretation. For example, here’s another interpretation of the tq-system, now into the context of divisions:

```
t  ⇒ equals
q  ⇒ divided into 
-  ⇒ one
-- ⇒ two
```

and so on, so that --t---q------ now interprets to “two equals three divided into six.” In a case like this, it’d be a mistake to argue about what the “true meaning” of --t---q------ is; the correct takeaway is that both meanings are encoded simultaneously. Even this simple example of a double-entendre is somewhat interesting: it demonstrates that the structure of multiplications is “the same” as the structure of divisions (borrowing a word from mathematics, Hofstadter would say that multiplications and divisions are “isomorphic”).

  

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107169/GEBpost/GEBimg3.png)

The cover art is a real photograph of two carved blocks of wood. Depending on which interpretation (angle of the light) you use, you can pull three different meanings out of each block.

Second, not all strings of the tq-system come out meaningful under interpretation. The tq-system also contains strings like ttq-t which don’t correspond to any multiplication. Let’s call a string *well-formed* if it does carry meaning under our choice of interpretation. This includes strings like -t-q-- which do mean something (one times one equals two) even though that something is false.

And third, all of the *theorems* of the tq-system are not only well-formed, but they also represent true multiplications. For example the theorems -t-q- and --t---q------ interpret to the true multiplications "one times one equals one" and "two times three equals six." (The well-formed string -t-q-- doesn’t, but that’s fine because it’s not a theorem.) This is really important, so let’s make it a requirement: if I call something an “interpretation” of a formal system, **I will always mean that** **the theorems are well-formed and come out true** under the interpretation.

For a counterexample, if we changed ‘-’ to mean “two,” then we wouldn’t have an interpretation anymore since the theorem -t-q- would represent the multiplication "two times two equals two," which isn't two – achem excuse me – true.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107195/GEBpost/GEBimg4.png)

As a final half-example of a formal system, let's augment the tq-system so it can prove theorems representing statements like "6 is composite."

The tqCP-system:

- Allowable characters: t,q,-,C,P
- Axioms: same as tq-system
- Rules: same as the tq-system, plus
	- Rule III: given a string *x* t *y* q *z* where *x*,*y*,*z* consist of at least two hyphens, you can form C *z*

The interpretation I intend for the tqCP-system into the context of “arithmetical statements” looks the same as the tq-system, plus:

```
Cx ⇒ x is composite
Px ⇒ x is not composite (or equivalently, x is prime)
```

What’s up with having a P when the inference rules don’t allow it to appear in theorems? More on that later.

## II. Jumping out of the system

I claimed above that the given interpretation of the tq-system was valid, i.e. that it transforms theorems of the system into true multiplications. How do I know that? Sure I gave two examples, the theorems -t-q- and --t---q------, but how can I be sure that every one of the infinitely many theorems of the tq-system interpret to true multiplications?

I’ll argue like this. First of all, the axiom -t-q- interprets to a true multiplication (one times one equals one). Second, we note that given a string *x* t *y* q *z* which represents a true multiplication (*x* times *y* equals *z*), rule I produces a string which represents a true multiplication ((*x* plus 1) times *y* equals *z* plus *y*). Same goes for rule II. As our axioms are true and our rules of inference preserve truth, all of our theorems must be true as well!

Where did the reasoning in the last paragraph take place? It certainly wasn't a proof "inside the tq-system," since those proofs just look like lists of tq-strings which obey the inference rules. Rather, it was an example of "stepping outside of the system." We reasoned *about* the tq-system using ordinary reasoning, not the internal formal logic of the tq-system. After all, the system doesn’t “know” about the interpretation we've given it – that is, our choice of interpretation has no bearing on tq-system’s axioms or inference rules, which are the only things that determine which strings are theorems. So we can't possibly hope to prove the validity of the interpretation by working within the tq-system. We had to step outside.

Here's another example of stepping outside the system. We just saw that every theorem of the tq-system represents a true multiplication. In fact, the converse is also true, namely that every true multiplication is represented by a theorem of the tq-system! If you're interested, you may wish to prove this – it will require stepping outside the system. Then, using this observation, you can derive theorems of the tq-system "from the outside." For example, since ---t---q--------- represents a true multiplication, we know that it must be a tq-theorem. Again, this isn't a "proof" in the formal sense, because a proof is a sequence of tq-strings produced by applying rules. It is a proof (in the informal sense) from outside the system.

Hofstadter points out that jumping outside the system is an important feature of intelligence. Before I introduced the tq-system I told you what my intended interpretation was. But even had I not, it's very likely you would have discovered it after a few minutes writing down tq-theorems. Instead of mindlessly churning out an ever longer list of theorems, you would instead gradually notice the patterns, put down your pencil to think, and discover that you can predict what all the tq-theorems are without writing them down. These are all outside-the-system activities.

Even now, you’re likely making frequent jumps out of your “reading this book review” system. Perhaps you’re pausing to check if you’re thirsty or need to go to the bathroom. And perhaps now you’re asking yourself if it counts as jumping out of the system if I just told you to do it. And maybe you’re now trying to do something I didn’t tell you to do just to prove that you really can jump out of the system. (sorry)

Contrast this with the behavior of a graphing calculator running a basic program that prints out a list of tq-theorems. The graphing calculator will never stop executing its code, step back to survey the data, notice the pattern, and print out IT'S THE MULTIPLICATIONS YOU DUMMY. Of course a human is ultimately some program, albeit a very complicated one running on an extremely powerful computer. Accordingly, there is some system out of which we are unable to step, the same way biological evolution is unable to step back, take a look at the data, and shout into the void [JUST KEEP MAKING MORE CRABS](https://xkcd.com/2314/) YOU DUMMY. The point isn't that human intelligence is "special" in some way that purely mechanistic reasoning can never replicate. The point is simpler: intelligent systems seem to be able to identify and run subtasks, as well as to monitor these subtasks from the outside and determine when to stop doing them.

## III. Truth vs. provability

> "Snow is white" is true if and only if snow is white.
> 
> – Alfred Tarski

At this point, it’s possible you’re mixing up the notions of truth and provability. If so, don't feel bad: so did literally everyone for the whole history of logic until 1930. That's when German logician Kurt Gödel announced his namesake *Incompleteness Theorem*, a consequence of which is that truth and provability really must be considered as separate notions. A goal of GEB part I, and of this book review, is to outline the key ideas going into this theorem. In this section I'll explain the distinction between truth and provability and state Gödel's theorem. But first, a story about Gödel.

Life in late 1930s Europe wasn't treating Gödel well. For one, he was unable to find an academic position because he had too many Jewish friends (a common side-effect of being a mathematician). And to make matters worse he had been conscripted to the German army. So Gödel did the logical thing: he fled to the U.S., got a position at Princeton, and hung out with his buddy Albert Einstein (who confessed that the only reason he showed up to work was for "the privilege of walking home with Gödel.") While studying for his U.S. citizenship exam, Gödel claimed to have discovered this one weird trick for legally turning the U.S. into a dictatorship (anti-fascists hate him!). Despite Einstein's warnings to Definitely Not Bring That Up, Gödel totally Brought It Up during his citizenship interview. Fortunately, Einstein, who was there serving as a witness and also knew the interviewer, managed to smooth everything over. Gödel became a citizen. I'm not sure what the moral is, but hopefully this gives you a taste of the mind of Kurt Gödel.

Okay, back to the logic textbook masquerading as a book review. A good way of thinking about the truth/provability distinction is that provability comes from the formal system and truth comes from the interpretation+context.

Provability is simpler, so let's tackle it first. Calling a string in a formal system *provable* is just a fancy way of calling it a theorem. That is, “provable string” and “theorem” are synonyms. This should make sense: remember that "theorem" just means something you can deduce from the axioms using the inference rules, i.e. something you can "prove." For example, the strings -t-q- and C------ are provable in the tqCP-system, but -t-q-- is not. In the MIU-system, MI and MUIIU are provable but (spoiler!) MU is not. Note that provability is a purely formal notion, i.e. it depends only on the formal system and not on whatever interpretation you attach to it.

Truth on the other hand relies on a choice of interpretation. Given a formal system with an interpretation, we say that a string of the system is *true* if it comes out true under the given interpretation. For example, --t---q------ is true because two times three does equal six, but P---- is false because four isn’t prime. We can't say whether MIII or MMU are true because we don't have an interpretation for the MU-system in mind.

Since by fiat all of our interpretations translate theorems to true statements, we know:

> in a formal system with an interpretation, all provable strings of the system are also true.

Or more succinctly: if provable then true. This is really important: it's why mathematicians and physicists can write funny symbols on paper, do logic on them, produce some new arrangement of funny symbols, and be confident that the new symbols actually tell them something true about the universe!

You might be tempted to believe the converse: that every true statement in a formal system is also provable. (Or at least, you might have been tempted to think that if I didn't have a whole section titled "truth vs. provability".) But consider the string P-- of the tqCP-system, which interprets to "two is prime." This string is certainly true, since two is prime. But it is *not* provable in the tqCP-system – in fact, none of the rules of the system allow you to produce a theorem with the character P.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107224/GEBpost/GEBimg5.png)

You're probably thinking that this demonstrates that the tqCP-system is *bad* in some way, or at least woefully *incomplete*. Perhaps you're tempted to augment the tqCP-system by adding a new rule: if for some *x* consisting of only hyphens, C *x* is not a theorem, then P *x* is a theorem. But there's an issue here: applying this rule requires making a list of all (infinitely many) theorems of the tqCP-system and checking that C *x* is not among them. But this is not the sort of simple, mechanistic rule that our formal systems are allowed to have – you could never finish writing down all the theorems and checking that C-- is not among them. You might be able to show *from outside the system* that C-- is not a theorem, but such "outside the system" reasoning has no bearing on provability *inside* the system.

Fear not: Hofstadter does explain a way of augmenting the tqCP-system to be able to prove statements like P-- (though it requires adding new characters as well as new rules). So *now* can we admit that the tqCP-system is no-good, and that we should root out all formal systems that can’t prove all their truths and replace them with ones that can?

If only! Gödel doesn't tolerate citizenship interviewers ignorant about weird tricks for making dictatorships, and he won't tolerate our nonsense either. Here is his theorem.

**Gödel's Incompleteness Theorem:** any sufficiently rich formal system, together with an interpretation, has strings which are true but unprovable.

A formal system which *is* able to prove all of its truths is called "complete." So Gödel's theorem says that every sufficiently rich formal system is incomplete – there will always be unprovable truths. What does “sufficiently rich” mean? It means “expressive enough to permit certain types of self-reference”; more on that in the next section.

## V. Self-reference and the proof of Gödel's theorem

Suppose that I were to walk into your room and say:

> This sentence is a lie.

As I’m an untrusted stranger, you might suspect that I’m lying. But if that were the case, then "This sentence is a lie" would be the truth, so I’d be telling the truth... a contradiction! Likewise, if you suppose I’m telling the truth, you'll come to find that I’m lying, another contradiction. (And at this point you should step out of your “solve logic puzzle” subtask and initiate a “report intruder to the police” subtask.)

This is called the liar's paradox, and it’s the basic idea behind the proof of Gödel's theorem. The core of the issue is that we have a system (the English language) trying to model itself, and we’ve exhibited a sentence whose interpreted meaning references that very same sentence. This snake-eating-its-own-tail pathology can be arranged to create other [similar paradoxes](https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox).

You might think that we can fix things like this with a simple rule like “no interpretation of a formal system can have the context be that very same system.” Unfortunately, things aren't so easy. Consider the following two-step version of the liar's paradox.

> The German sentence below is false.
> 
> Der obige englische Satz ist wahr. ("The English sentence above is true.")

Here, the system "sentences in English" has an interpretation expressive enough that sentences in English are able to make claims about arbitrary sentences in German. But the same is true about the system “sentences in German” being expressive enough to make claims about arbitrary sentences in English. And although each sentence by itself is perfectly harmless, the whole is paradoxical!

(Note that “sentences in English/German” are not really formal systems in the sense defined before, but they are similar in the sense that they are collections of strings which can be endowed with interpretations which give the strings meaning. So the above should be taken as a purely informal illustration of the ideas to be fleshed out below.)

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107251/GEBpost/GEBimg6.png)

Drawing Hands, by M.C. Escher, an illustration of the two-step liar’s paradox.

Part of the issue is that English is *too rich*. That is, it's able to talk about concepts like "truth" and "falseness" as well as support self-reference. It’s also rich enough to model systems (like German) which are themselves rich enough to model English, enabling the two-step liar’s paradox. These aren't issues that are easy to patch; it's not clear how much of English we would need to remove to make it "not too expressive." Perhaps in doing so, we would destroy our ability to say anything useful.

English is too fuzzy to work with, so instead Gödel works with statements of number theory – things like "two plus two equals four" and "four is a factor of eight." It ends up that while number theory isn’t expressive enough to talk about the *truth* of number-theoretical statements, it is expressive enough to talk about the *provability* of number-theoretical statements.

(I won’t cover it further in this review, but the deeper reason that number theory is expressive enough to talk about provability is that it is able to support recursion (the key fact being that “theorems” are strings which arise from recursively applying rules). Going deeper, the reason number theory can do recursion is because it has an axiom of *induction*.)

The idea of Gödel's proof is to encode a “provability version” of the liar's paradox into number theory. That is, given a formal system rich enough to model number theory, Gödel comes up with a string *G* of the system whose meaning under interpretation is:

> *G* is not provable.

If *G* were false, then *G* would be provable and hence true, a contradiction. So *G* must be true, making it an unprovable truth. It follows that the formal system in question is incomplete.

The rest of this section fleshes out this idea in more detail, using an idea called Gödel numbering. I think it’s pretty cool, but if it’s not your cup of tea, feel free to skip to part VI.

As a warm up, recall the MU puzzle from above: determine whether MU is a theorem of the MIU-system. I will now demonstrate that the answer is "no – MU is not a theorem." The idea is to encode "MU is a theorem of the MIU-system" as a claim about number theory, and then figure out if that claim about number theory is true.

To do this, let's first transform strings of the MIU-system into numbers by the rule:

```
M ⇒ 3
I ⇒ 1
U ⇒ 0
```

For example, MIUUI is the number 31001, MU is the number 30, and the axiom MI is the number 31. Under this transformation, the rules of the MU-system can be stated arithmetically. For example, rule I says that if a number has units digit 1, then you may multiply it by 10 (thereby appending a 0 to the end). Or more formally:

> given a number of the form 10 *m* + 1, you may form the number 10\*(10 *m* + 1).

You can do the same thing for the other rules too.

Let's call a number which corresponds to a theorem of the MIU-system a MIU-number. So we've transformed the claim "MU is a theorem of the MIU-system" to the equivalent claim "30 is a MIU-number," which can also be stated as “30 can be formed from 31 by repeatedly applying such-and-such arithmetical operations.” This might not seem like progress, but it is! The claim "30 is a MIU-number" is a *number theoretical statement* (though perhaps not an interesting one). In essence, it’s similar to – but more complicated than – the more familiar statement “216 is a power of 6” i.e. “216 can be formed from 1 by repeatedly applying the multiply-by-6 operation.”

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107282/GEBpost/GEBimg7.png)

Now we can dispose of the MU puzzle by proving a proposition about MIU-numbers:

**Proposition:** No MIU-number is divisible by 3.

I’ll leave the proof to you – it’s not hard, especially if you remember [the rule](https://en.wikipedia.org/wiki/Divisibility_rule#Divisibility_by_3_or_9) for checking whether a number is divisible by 3.

Since MU corresponds to 30, which *is* divisible by 3, we deduce that 30 is not a MIU-number. Hence MU is not a theorem of the MIU-system, and we’re done. If you're rightly baffled, you can press pause on your computer screen now to reflect deeply on what’s happened. You can press play when you're ready to resume the proof of Gödel's theorem.

The procedure above turned strings of the MIU-system into numbers, and claims about those strings into statements of number theory. This is called *Gödel numbering*, and it can be done to any formal system. Via Gödel numbering, the claim "MU is a theorem" *about* the MIU-system corresponds to the number-theoretical claim "30 is a MIU-number.” In other words, despite the MIU-system having no interpretation that gives its strings meaning, Gödel numbering gives number-theoretical meaning to certain claims *about* the MIU-system.

Could something interesting happen if we Gödel number a system that *already has* an interpretation into number theory? Could the meaning acquired through the interpretation clash with the meaning induced by Gödel numbering? Could my rhetorical questions get any more leading? Is the answer to all of these yes?

In GEB, Hofstadter spends two chapters constructing an explicit example of a formal system that models number theory, called Typographical Number Theory, or TNT (foreshadowing that it will blow itself up). For the sake of concreteness, he then proves the Incompleteness Theorem for the system TNT. Nevertheless, the same proof works for a general formal system *S* with an interpretation into number theory, and I’ll explain it here in this more general language.

(here comes the technical meat; please set your brains to “think very hard”)

Suppose we are given a formal system *S* with an interpretation into number theory. And suppose that the formal system is "rich enough" in the sense that any statement about number theory can be rendered as a string of *S*. We want to show that *S* has an unprovable truth. Fix a Gödel numbering for *S*, i.e. a correspondence between characters of *S* and digits which turns all the strings of S into numbers and all the rules of *S* into arithmetical rules. As before, let's call a number an *S* -number if it corresponds to a theorem of *S*.

Given a string *G* of the system *S*, let *g* be the number corresponding to *G* under the Gödel numbering. Now, " *G* is not a theorem of *S* " is equivalent to the number-theoretical claim " *g* is not an *S* -number.” But the number theoretical claim " *g* is not an *S* -number" can in turn be rendered as a string of *S* (as can any number theoretical claim, by assumption). Let's call this string *G'*.

In a situation like this, Gödel gave a magic recipe (or see chapters 13 and 14 of GEB) for cooking up a specific string *G* such that the resulting *G'* *is the same as* *G*. Thus, this *G* interprets to the statement “ *g* is not an *S* -number,” which is true if and only if *G* is not a theorem of *S*. Informally, we might say that *G* carries the meaning “ *G* is not provable in *S*.” And now we’re done: if *G* is false, then G *is* a theorem of S, and is therefore true, a contradiction. So *G* is true, and thus *G* is not provable. Thus *G* is an unprovable truth and *S* is incomplete. Q.E.D.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107318/GEBpost/GEBimg8.png)

I'll end this section with an exercise for those interested: how is this proof like the proof of undecidability of the halting problem? (For solutions, please consult *Gödel, Escher, Bach* by Douglas Hofstadter.)

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107341/GEBpost/GEBimg9.png)

Fine, I’ll tell you about the RNA transcription = Gödel numbering thing. But if you think this is the extent of the analogy, then let me tell you about this one book by Douglas Hofstadter.

## VI. GEB Part II

As a math grad student, I’m not a bad person to write a book review of GEB part I. On the other hand, I’m vastly unqualified to say anything about GEB part II. Buuuut I’ll say a bit anyway.

My executive summary of GEB part II is: you know all those cool ideas about self-reference, meaning, etc. in part I? Those all have something to do with intelligence and consciousness.

This is obviously a really bad summary. One issue with it is that large chunks of part II are devoted to completely uncontroversial topics like a short history of computing and artificial intelligence, an explainer of Gödel’s “magic recipe” mentioned above for producing the string *G*, and a refutation of incorrect takeaways from the incompleteness theorem like “artificial intelligence is impossible.”

That said, it’s pretty clear that Hofstadter’s main goal for part II is the stuff about intelligence and consciousness; all the other topics are tangential. My overall sense is that Hofstadter’s most interesting ideas here have not aged well since GEB’s 1979 publication. Here’s a sampling of his claims:

1. While he avoids positing the existence of a so-called " [grandmother neuron](https://en.wikipedia.org/wiki/Grandmother_cell) " – that is, a neuron whose sole job is to fire whenever you need to make use of the concept "grandmother" – Hofstadter does seem to think that something kinda like this is true: that there is a "grandmother module" in the brain – perhaps a collection of neurons – which activates whenever you think of a grandmother (and doesn’t activate for other things).
2. Hofstadter seems to believe that the way we think thoughts is for all of our various modules to fire together in roughly the same way that a bunch of words are said together to form a sentence. E.g. the thought "My grandmother is happy" boils down to the modules in your brain representing "grandmother" and "happy" activating together, along with some additional information to specify that it is “my grandmother” instead of just “a grandmother” and things like that.
3. His paradigm of (artificial) intelligence seems to involve intelligent systems constructing formal systems which model the problems they’re trying to solve, and then solving the problems by working symbolically with the formal system. More specifically, he seems to imagine that intelligent systems: construct a network of concepts and their interrelations (similar to what [WordNet](https://en.wikipedia.org/wiki/WordNet) does for languages) in which the concepts are internally represented by modules like the grandmother module above; then treat the modules like symbols in a formal system, manipulating them according to certain rules, thereby modifying the relations between them.
4. Per Hofstadter, consciousness arises in systems which support self-reference and are able to self-modify in certain ways. Examples: computers which are able to edit their source code, neural nets in which the current weights determine how the weights are modified, and human brains in which higher-level abstractions affect the way we think about lower-level abstractions and vice versa. Hofstadter calls these self-referential systems “tangled hierarchies” and the way in which they self-modulate “strange loops.”

Idea 1 seems right when it comes to visual processing. At a low level, we’ve identified particular neurons that fire together in certain ways to encode information about the orientations of lines., which is kinda like a low-level version of a grandmother module for the concept of vertical-ness or whatever (though apparently [predictive processing](https://slatestarcodex.com/2017/09/05/book-review-surfing-uncertainty/) has another take on what information exactly is being represented). At a medium level, there are neurons that selectively fire when you see pictures of faces, animals, or scenes. At a high level … it’s unclear. Some people interpret the work of Quiroga *et al* as demonstrating the existence of a “Halle Berry” neuron, but per [Wikipedia](https://en.wikipedia.org/wiki/Grandmother_cell), Quiroga himself disputes this interpretation. But we *do* know that high-level modules like this exist in some artificial neural networks: [OpenAI has found](https://openai.com/blog/multimodal-neurons/) individual neurons in their CLIP neural net which seem to correspond to concepts like “Spiderman,” “winter,” or “West Africa.” It perhaps shouldn’t be so surprising that modules like this exist for visual processing – you can experience them activating firsthand when you look at a blurry picture and it all-of-a-sudden resolves into a face.

Beyond visual processing, things aren’t so clear. Your “face module” activates when you *see* a face, but does it activate when you think about the concept of a face? I’m personally skeptical. Our current understanding of GPT-3 is – I think – as an uninterpretable jungle of weights in which no single concept is localized to a particular part of the network, which seems like evidence against. But if there are major advances in AI interpretability, such that you can determine whether GPT-3 is thinking about a grandmother just by tracking the activation of a particular cluster of neurons, then that would be a different story.

Idea 2 – that thought arises from certain interactions among our hypothetical brain modules that mimic the interactions among words in sentences – goes further into murky territory. It first requires the existence of grandmother modules not just for visual processing but for cognition in general, which, again, seems incompatible with the uninterpretable jungle of neurons that comprise our best artificial minds. Then it’s an even stronger claim above-and-beyond that! If it were true, it would imply that advanced AI interpretability could not only detect the concepts that GPT-3 is utilizing, it could *read GPT-3’s mind* and write down in English what GPT-3 is thinking. Even if you interpret Hofstadter’s claims as being only about human brains, which are probably more interpretable than GPT-3, this stretches my credulity. Nothing here is impossible or definitively disproved, but it overall seems like a paradigm that’s a bad match for our modern understanding of the brain.

It’s hard for me to comment on idea 3 – the idea that intelligent systems work by constructing formal systems to model the world and then manipulating these formal systems to generate new data/predictions/whatever – because I don’t know how literally Hofstadter wants us to take him here. Again, my first instinct is to gesture frantically at GPT-3, which can write ([and draw](https://openai.com/blog/dall-e/)) better than most people I know, but fails at multiplying large numbers. If GPT-3 secretly works by constructing a super complex formal system that models the human-produced text in its training data, why didn’t it come up with a much simpler formal system (like the tq-system) for modeling the multiplications in its data?

That said, Hofstadter specifically addresses the question of whether AIs will be good at addition. He says they might not be. (Of course, this *must* be the right answer since I’m an intelligent system, I frequently fail to subtract 6 from 11, and there’s no reason to rule out that AIs could be the same; Hofstadter is aware of all this.) Hofstadter doesn’t seem to think this poses an issue for his model of how intelligent systems work, but it seems like it should? Did I just take all the stuff about grandmother modules and manipulation of symbols literally when he meant it all as an illustrative example? I’m honestly wondering if I misunderstood his point entirely.

In any case, I don’t think there’s a way of understanding Hofstadter’s ideas here that doesn’t involve Hofstadter’s model being pretty surprised by modern ML. Inventing better data structures for modeling the world and better procedures for refining and applying these models? Hah, that’s for chumps. *Real* intelligence comes from throwing ever-larger neural networks at data and letting them do uninterpretable nonsense with it.

Finally, idea 4 – that consciousness arises from tangled hierarchies and strange loops. You can think about this as a souped-up version of the idea that consciousness fundamentally arises from self-awareness (i.e. “you are dust which is aware that it is dust and is therefore more than dust”). Except Hofstadter replaces “self-awareness” with the more nuanced concept of a formal system being self-referential and self-modifying. I’m not sure this modification does anything to clarify the idea. Hofstadter clearly struggles to say exactly how strange loops lead to consciousness, and when he comes closest to addressing the issue he’s uncharacteristically brief, writing that conscious experience “comes from the vortex of self-perception in the brain.” Okay, cool, glad that’s settled.

For now, I tentatively conclude that Hofstadter is playing the “ [Gödel’s theorem and consciousness are both mysterious and therefore equivalent](https://www.smbc-comics.com/comic/the-talk-3) ” game. If there's some way to salvage Hofstadter's ideas in part II, someone other than me will have to write the book review doing it.

![](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1663107366/GEBpost/GEBimg10.png)

Relativity, by M.C. Escher. Like GEB, this drawing makes more sense if you only look at half of it.