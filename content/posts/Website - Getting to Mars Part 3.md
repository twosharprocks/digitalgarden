---
title: Website - Getting to Mars Part 3
created: 2026-01-26
updated: 2026-07-17
status: evergreen
draft: false
tags:
  - writing
related: "[[Writing]]"
source: https://web.archive.org/web/20170617195929/http://joshrichards.space/category/space/
author:
  - Josh Richards
published: 2017-04-28
---
![](https://web.archive.org/web/20170617195929im_/https://i0.wp.com/joshrichards.space/wp-content/uploads/2017/04/Raptor-test-9-25-2016.jpg?resize=400%2C266)

We kicked off my series on [“Getting to Mars”](https://web.archive.org/web/20170617195929/http://joshrichards.space/2017/02/27/space-getting-to-mars-part-1-overview/) last time with a look at [Orbital Mechanics](https://web.archive.org/web/20170617195929/http://wp.me/p855lB-6N) – showing that the physics of getting from one planet to another can be mostly explained with [a stapler, a pen, and Kristen Wiig looking unimpressed](https://web.archive.org/web/20170617195929/https://www.youtube.com/watch?v=lcyfDRYKDJM). This time we’re looking at the propulsion systems that we’ll use to get to Mars.

Of course because every armchair expert has their own pet propulsion project they think is critical to the future of space exploration, this is probably the article I’ll have to delete the most hate-mail for. That’s right – I don’t even read your unsolicited and poorly-spelled bullshit before deleting it, but thank you for reading all of mine! And if you haven’t already figured it out this is also the article you’re probably going to get me at my snarkiest, because there are three phrases I hear on a fairly regular basis that genuinely get under my skin and strangely all three are connected in some way to spacecraft propulsion…

**#1 “Space is hard”** – The lame catch-cry of everyone that’s just watched a spacecraft disintegrate in a “[rapid unscheduled disassembly](https://web.archive.org/web/20170617195929/http://www.urbandictionary.com/define.php?term=Rapid%20Unscheduled%20Disassembly)“. Don’t whinge that space is “hard” – find the cause of the problem and learn from it. Space isn’t hard, it’s just unforgiving of screw-ups. Screw-ups like when [someone puts in a gyroscope upside down on a US$1.3 billion rocket launch](https://web.archive.org/web/20170617195929/http://www.russianspaceweb.com/proton_glonass49.html#culprit), or when someone else [loses a Mars probe](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) because it was built by the [world’s biggest aerospace contractors](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Lockheed_Martin) in the [only country besides Liberia & Myanmar **still** fighting the Metric system](https://web.archive.org/web/20170617195929/http://www.ibtimes.com/america-liberia-myanmar-anti-metric-system-holdouts-1109357).

**#2 “It’s not rocket science”** – The sarcastic accusation that something you’re struggling with isn’t really that difficult. You know, instead of _helping you_, someone will suggest you’re an idiot. Here’s something for all of you unhelpful jerks: Rocket science is **not** difficult. Rocket science can be explained with [literally **ONE** equation](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation) (aptly called the “Rocket Equation”) that’s not even remotely complex. Ready for it
![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/rocket-eq.jpg?resize=131%2C53)Where ![\Delta v\](https://web.archive.org/web/20170617195929im_/https://wikimedia.org/api/rest_v1/media/math/render/svg/28563b5d468baab12a7d33b49cac197c2c1ed885)is the change in the spacecraft’s velocity, ![v_{\text{e}}](https://web.archive.org/web/20170617195929im_/https://wikimedia.org/api/rest_v1/media/math/render/svg/a0ad4222c764f1a57fe3e1f48d1e24419ea8ebfa) is how fast things are being shoved out the back of your spacecraft (eg. the rocket exhaust), and you multiply that by the natural logarithm (![\ln](https://web.archive.org/web/20170617195929im_/https://wikimedia.org/api/rest_v1/media/math/render/svg/c0de5ba4f372ede555d00035e70c50ed0b9625d0)) of your spacecraft’s initial mass (![m_{0}](https://web.archive.org/web/20170617195929im_/https://wikimedia.org/api/rest_v1/media/math/render/svg/3a6ff51ee949104fe6fae553cfbdfba29d5fac1e)) over it’s final mass (![m_{f}](https://web.archive.org/web/20170617195929im_/https://wikimedia.org/api/rest_v1/media/math/render/svg/a6b1ed1cca247d7fbe5a237f3c266a4e13850185)). You can also express the same equation in terms of [specific impulse](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Specific_impulse), but if it’s all feeling too complex just remember **you go faster if you throw bits of your spaceship out the back really fast to make it lighter**.

Rocket **science** is not difficult, however rocket **engineering is** ludicrously complex and exceptionally challenging*. So next time you decide to be an obnoxious and holier-than-thou wanker to someone trying to do something they’re struggling with, how about at least getting the terminology right?

_*For why I still refuse to say rocket engineering is “hard”, see point 1 above_

**#3 “We need to develop better solar electric propulsion to get to Mars”** – I’ll get to why you’re what’s wrong with the space industry a little later, but for now lets just say you’re a piece of shit and I can prove it mathematically.

Spacecraft propulsion can be broken down into two big categories: **Thermodynamic** (using heat to move gas) and **Electrodynamic** (using electricity/magnetism to move gas).

## **Thermodynamic**

This category is mostly the kind of spacecraft propulsion everyone is familiar with: rockets.![](https://web.archive.org/web/20170617195929im_/https://i1.wp.com/joshrichards.space/wp-content/uploads/2017/04/rocket.jpg?resize=400%2C250)Absolutely no one is doubting that rockets look super cool. They’re also dangerous, wasteful, noisy, and prone to going boom because of the most tiny and obscure things… like [super-chilled liquid oxygen turning solid on your carbon-fiber wrapped helium tanks.](https://web.archive.org/web/20170617195929/http://www.theverge.com/2016/11/5/13533900/elon-musk-spacex-falcon-9-failure-cause-solved)

Rockets are also _**ridiculously**_ expensive and absurdly inefficient at getting things to space. The Saturn V that launched men to the Moon* weighed nearly 3 million kilos on launch, but only 5,560kg of that was left by the time the Command Module splashed down in the ocean. To put it in context, **0.185% of the original rocket’s mass came back to Earth and the other 2,964,440kg was either burnt as fuel, dumped in the ocean/space, or left on the Moon**. Considering each Saturn V launch cost about US$1.16 billion in 2016 figures, that’s a whole lot of specialised and expensive stuff to be just throwing away.
_* Don’t even start with me Moon Hoaxers – I will destroy you_

I’d talk about how NASA’s “Space Launch System” is supposed to (eventually) be more powerful than Saturn V… buuuuuuuut since SLS & the Orion capsule are basically the worst parts of the [Bush-era Constellation program](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Constellation_program) that have already cost US$18 billion and are now projected to reach US$35 billion in 2025, at this point it really looks like it’s just a [pork-barreling jobs program](https://web.archive.org/web/20170617195929/https://www.buzzfeed.com/danvergano/nasa-is-a-jobs-program?utm_term=.aeqaJQV3X#.tvY5kapRW) for a bundle of US Senators through the old conservative aerospace manufacturers. A jobs program which is also takes funding away from **real** exploration opportunities (like the underfunded [Commercial Crew Program](https://web.archive.org/web/20170617195929/http://www.slate.com/blogs/bad_astronomy/2015/08/24/congress_and_nasa_commercial_crew_program_is_underfunded.html)) to build a rocket that’s going anywhere.

I currently have a bet with a fellow space geek about SLS: I’m convinced it will be cancelled before it ever flies, whereas she thinks it’ll fly _once_ before it’s cancelled. The loser has to buy the other a ticket to Mars aboard this…

Did you see that **gigantic rocket** flying itself back to the launch pad **_to refuel and launch again_**_**?**_ That’s SpaceX’s [“Interplantary Transport System”](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/SpaceX#Interplanetary_Transport_System), and once it’s up and running in the 2020’s there will be several of these taking **100 to 200 people to Mars every few years for about US$200,000 each – return trip included**. They can afford to talk about sending people to Mars and back for [less than the median cost of a house in the US](https://web.archive.org/web/20170617195929/https://www.google.com.au/search?q=median+house+price+US&oq=median+house+price+US&aqs=chrome..69i57j0l5.9036j1j4&sourceid=chrome&ie=UTF-8) (or 1/4 of a house in Sydney) because they’re not dumping most of their rockets into the ocean every time they launch – [they’re landing them, refueling them, and **launching them again**](https://web.archive.org/web/20170617195929/https://www.youtube.com/watch?v=qXzyrTQoNYs). Building better rockets and not throwing most of them away after a launch means the cost of getting stuff to orbit has decreased dramatically in recent years.

![](https://web.archive.org/web/20170617195929im_/https://i1.wp.com/joshrichards.space/wp-content/uploads/2017/04/better.jpg?resize=400%2C400)

We’ve never used rockets for their efficiency though – we use them because they produce a huge amount of _thrust_. If you have to get something from the ground into Low-Earth Orbit, it needs to push through the air with enough raw power and velocity to break free of the atmosphere and start falling around the Earth with enough velocity not to hit it again. Right now the only thing we’ve got that can push hard and fast enough to reach orbit is rockets, and no matter whatever weird propulsion system other folks might be dreaming about this is also the only way we’re going to get to Mars in the next 15-20 years*.

_*Bring it on Solar Electric Propulsion people – I’ve got your number at the end of this article._

That’s not to say all rockets are the same though – we’ve got all sorts of different ways of making things go boom to get somewhere fast:

**Solid Rockets** – Basically really big and complex versions of the little gunpowder rocket engines you can buy at a hobby store. They’re cheap, powerful, and easy to make – perfect for launching things like [cargo and probes into space](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Solid-propellant_rocket#Orbital_rockets).![](https://web.archive.org/web/20170617195929im_/https://i1.wp.com/joshrichards.space/wp-content/uploads/2017/04/SLS-booster.jpg?resize=400%2C208)

It’s probably not a great idea to use solid rocket boosters on anything carrying people though – once you light a solid rocket you can’t stop it burning if something goes wrong… like when one on the space shuttle [burned through an o-ring and into a 760,000kg tank fuel of rocket fuel, which then exploded and killed seven astronauts](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster). But NASA is planning to use solid rocket boosters again [with the crewed SLS](https://web.archive.org/web/20170617195929/https://www.nasa.gov/press-release/nasas-space-launch-system-booster-passes-major-milestone-on-journey-to-mars) (test fire pictured above). So, you know… YOLO.

**Liquid Rockets** – Pumping flammable liquids into a chamber and having them explode in a specific direction. While the Chinese were the first to get serious about [solid rockets back in the 1200’s](https://web.archive.org/web/20170617195929/https://www.grc.nasa.gov/www/k-12/TRC/Rockets/history_of_rockets.html), it wasn’t until the 1900’s that a guy called [Robert Goddard](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Robert_H._Goddard) started to set fire to liquids to push rockets around. Unfortunately the US’s scientific community and the New York Times just made fun of him for suggesting rockets could work in space.

![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/ny-times-correction-goddard.jpg?resize=424%2C238)

Correction the New York Times published 3 days before Apollo 11 launched (on liquid rockets) to the Moon… and 24 years after Goddard had died.

Fortunately **_some_** people payed attention to Goddard’s research into liquid rockets. Unfortunately those people were also the _**Nazis**_, who then used that research to bomb Europe with these:

![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/V2.jpg?resize=400%2C460)Liquid rocket engines are way more complex than solid rocket engines essentially because the fuel is sloshing around and needs to be pressurised through tanks & fuel lines for them to keep flying. Going back to my earlier “rocket science is easy, but rocket engineering is hard” – the national security restrictions imposed by each country on who can work on their rocket technology often has little to do with the rocket itself, and is almost entirely about protecting the technology behind the _[turbopumps](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Turbopump)_ that push the fuel and oxidiser at high speed & pressure into the engine bell.

Liquid rockets generally get broken down into two further categories depending on their fuel too. **Bipropellants** are what you see in a usual rocket launch where an oxidiser (usually liquid oxygen) and a fuel (kerosene, liquid hydrogen, methane, ect) burn to produce thrust. [**Monopropellant**](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Monopropellant) is a single liquid that ignites when it touches a catalyst, and is often used once you’re in space to turn your spacecraft around or give it a gentle push. It’s also usually made of hideously toxic, carcinogenic and explosive liquids like [Hydrazine](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Hydrazine), that apparently smells like fruity-ammonia [if you live long enough to tell someone](https://web.archive.org/web/20170617195929/http://www.edotek.co.uk/just-how-dangerous-are-the-hydrazine-fuels/).

**Hybrid Rockets** – A surreal mix of a solid and liquid rocket. The most obvious and well-known example of a hybrid rocket powers this:

![](https://web.archive.org/web/20170617195929im_/https://i0.wp.com/joshrichards.space/wp-content/uploads/2017/04/Virgin2.jpg?resize=400%2C300)

Virgin Galactic’s Spaceship Two

Hybrid engines have a liquid/gas oxidiser that runs through channels in the solid fuel to burn it. They avoid the complexity of liquid rocket engines, and unlike a solid rocket you can stop them once they’re lit by cutting off the oxidiser supply. The downsides are they’re not as efficient as solid **or** liquid rockets, and most of them are _filthy_ polluters. The fuel going into hybrid engine in Spaceship Two has been changed a lot, but it’s usually [nitrous oxide burning _**rubber**_](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/SpaceShipTwo#Rocket_engine). So [pumping **soot** directly into the upper atmosphere](https://web.archive.org/web/20170617195929/http://www.popsci.com.au/science/space-tourisms-black-carbon-problem,379557) isn’t exactly fantastic for things like Global Warming…

**Nuclear Propulsion** – Launching tonnes of hot, radioactive material into space because it’s _really_ good at getting you places fast… provided it doesn’t explode on the way.

![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/500px-NASA-NERVA-diagram.jpg?resize=400%2C188)

Now I’m only including this because it _**is**_ a form of thermodynamic propulsion, people have talked about for more than 60 years, folks like NASA & the Soviets _**have**_ designed entire working systems around it… and even at it’s absolute safest it’s still fairly insane.

Nuclear rockets are outrageously powerful – even the most basic designs are twice as powerful as what’s possible with a chemical rocket. There are dozens of different (theoretical) varieties, however only two have ever been developed properly: [NASA’s NERVA](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/NERVA) and the [Soviet Union’s RD-0410](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/RD-0410). NASA actually had the closed-cycle [NERVA XE flight ready and deemed suitable for a Mars mission in 1969](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/NERVA#NERVA_XE), right before NASA’s funding was cut because it was clear the US was going to win the race to the Moon. Both the NASA and Soviet systems still involved using a flying nuclear reactor to super-heat hydrogen in space, however they were designed to be _comparatively_ safe [“closed cycle” systems](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Gas_core_reactor_rocket#Closed_cycle_designs).

I say comparatively, because you have to compare it to the other crazy shit other people were suggesting in the 1960’s. Fun things like [“open cycles” designs](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Gas_core_reactor_rocket#Open_cycle_designs) that used weapons-grade radioactive material and deliberately spewed out clouds of radioactive exhaust.

![](https://web.archive.org/web/20170617195929im_/https://i0.wp.com/joshrichards.space/wp-content/uploads/2017/04/nuclear_gas.jpg?resize=400%2C263)

See the bit saying “Uranium 235 T~55,000 K” leading to an open nozzle Because fuck everyone else on the planet, right?

Then there’s the folks who designed [Project Orion](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Project_Orion_\(nuclear_propulsion\)), who clearly felt the only thing better than using a nuclear reactor in space would be to use _[actual nuclear weapons](https://web.archive.org/web/20170617195929/https://www.businessinsider.com.au/project-orion-nuclear-bomb-propelled-spaceships-2015-6?r=US&IR=T)._ Project Orion was about literally firing a nuclear weapon behind your spaceship to propel it in the other direction: for anyone who’s ever played Quake or Team Fortress 2 this is [basically a rocket-jump](https://web.archive.org/web/20170617195929/https://www.youtube.com/watch?v=Nji_vEz8d_Y) _but with a nuke_.

We’re not talking about just one nuke either: the idea was to have one going off every second, and some of the interstellar designs called for a spacecraft **20km long** that carried **300,000,000 1-Megaton nuclear weapons,** or “pulse units” as they were so eloquently renamed. Strangely enough Project Orion pretty much ended when most of the world signed the “**Treaty Banning Nuclear Weapon Tests in the Atmosphere, in Outer Space and Under Water**” (aka the [Partial Nuclear Test Ban Treaty](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Partial_Nuclear_Test_Ban_Treaty)) in 1963.

![](https://web.archive.org/web/20170617195929im_/https://i1.wp.com/joshrichards.space/wp-content/uploads/2017/04/orion.jpg?resize=400%2C300)

The fever dreams of Dr Strangelove

Chances are we’ll need some sort of nuclear propulsion in the future to take humans _beyond Mars_ though. Jupiter barely gets 4% of the sunlight the Earth does, so the diminishing light from the Sun makes solar power a lot less viable. It’d also be a great way to reduce the nuclear stockpiles we have, and there’s even some semi-reasonable arguments for taking small nuclear power plants to provide electricity to a colony on Mars – the big issues are obviously what do you do with the waste and what if something breaks?

Nuclear propulsion isn’t _completely_ insane… but do we need to take the risk, when we can get to Mars just fine using conventional chemical rockets **No.**

Do you know what else we don’t need to get to Mars **Solar** Bullshit **Electric** Fucking **Propulsion**.

## **Electrodynamic**

Maybe you’ve heard on the news about some crazy space propulsion system that uses lasers, ions, or something else that sounds really complex and weird. Chances are it’s either a [solar sail](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Solar_sail) (which are slow but cool in their own [“Star-Surfing with Sagan”](https://web.archive.org/web/20170617195929/http://www.ibtimes.co.uk/lightsail-carl-sagans-solar-sail-spacecraft-concept-finally-realised-1500681) kind of way) or you’ve heard about some variant of an ion drive (which are also slow but cool in their own [“Star Trekking with William Shatner”](https://web.archive.org/web/20170617195929/https://www.youtube.com/watch?v=-OrXLIB05RY) kind of way too).

![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/Ion-Engine.jpg?resize=400%2C315)

Ion drives are not some far flung science-fiction fantasy though: [Harold Kaufmann built the first ion thruster in 1959](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Ion_thruster#Origins), the Russians launched their own variant [(known as a Hall Effect Thruster)](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Hall-effect_thruster) on a satellite in 1971, and almost all modern communication satellites use some form of ion drive for “station-keeping” – correcting for variations in Earth’s gravity to maintain a highly precise [“geo-stationary”](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Geostationary_orbit) orbit.

Essentially ion drives use electric fields to accelerate a gas (usually Xenon) out an exhaust at incredibly high velocities to produce a _tiny_ thrust. The high exit velocity (aka “Specific Impulse”) means ion drives are insanely efficient and capable of reaching much higher maximum velocities than any rocket ever could, and there’s been [some really exciting improvements](https://web.archive.org/web/20170617195929/http://www.smh.com.au/technology/sci-tech/mars-awaits-sydney-rocket-scientist-to-test-ion-drive-in-space-20150924-gjtzlc.html)… but because ion drives only throw out only a tiny bit of gas (eg. roughly the same amount of force you feel blowing on the back of your hand) they’re also _incredibly_ slow to accelerate up to those high velocities.

How slow NASA’s [Dawn mission](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Dawn_\(spacecraft\)) has three Xenon ion thrusters capable of 90mN of thrust (about the same force as the weight of a postage stamp) that can accelerate the probe from 0 to 100km/hr _**over four days**_.

![](https://web.archive.org/web/20170617195929im_/https://i2.wp.com/joshrichards.space/wp-content/uploads/2017/04/sloth.jpg?resize=236%2C281)

Ion drives absolutely have their place, but no matter what bullshit spin some of the old aerospace players might try to pull that place is **not** getting people to Mars. Ion drives _are_ improving, but unless [VASIMR unexpectedly gets a demo flight and proves it actually works](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Variable_Specific_Impulse_Magnetoplasma_Rocket#Research_and_development) electrodynamic propulsion simply won’t be powerful enough to shorten the trip to Mars for humans any time in the next few decades. _**Especially**_ if you’re only using solar power.

Improved ion drives that run on solar power _will_ be really useful however for… getting communication satellites from Low-Earth Orbit into a Geo-stationary orbit.

![](https://web.archive.org/web/20170617195929im_/https://i0.wp.com/joshrichards.space/wp-content/uploads/2017/04/geo-sat.jpg?resize=400%2C311)

Here’s a fun fact: the global satellite communication industry generates over **[US$200 billion in revenue each year](https://web.archive.org/web/20170617195929/http://www.sia.org/wp-content/uploads/2017/03/SSIR-2016-update.pdf)**, and makes up nearly 2/3’s of the **_entire space industry_**. Reaching Low-Earth Orbit (160km to 2000km altitude) with a rocket is relatively simple, however getting to Geo-stationary orbit (~36,000km and where almost all large communication satellites need to be placed) is much harder, requires far greater velocities, and usually needs an additional stage on the rocket. This extra velocity and additional staging brings greater risks of things going wrong, so naturally launching something to such a high orbit is also a _**lot**_ more expensive.

So if telecommunication companies can launch new satellites to a much cheaper Low-Earth Orbit and then use solar powered ion drives (aka “[Solar Electric Propulsion](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/Solar_electric_propulsion)” aka “The bane of my existence”) [to slowly shift new satellites up to geo-synchronous orbit over several months](https://web.archive.org/web/20170617195929/http://www.energymatters.com.au/renewable-news/em3041/), they’ll save literally **billions** in launch costs alone.

Are you bored by this yet?  ![](https://web.archive.org/web/20170617195929im_/https://i0.wp.com/joshrichards.space/wp-content/uploads/2017/04/chimp.jpg?resize=400%2C308)

No shit – the satellite communication industry is boring, but it’s also really big money. Do you know what is _**not**_ boring, but also means risking lives for something that won’t make anywhere near as much money? **SENDING PEOPLE TO MARS**.

Which is why there’s a huge amount of money and research going into solar electric propulsion at the moment, and why I roll my eyes obnoxiously at everyone who tells me it’ll “help with NASA’s journeytomars”. Because they either don’t understand how weak solar electric propulsion currently is, or they’re trying to bullshit me and others into believing a technology being developed to reduce the cost of deploying communication satellites around Earth will somehow get me to Mars.

I’m happy to be proven wrong on all of this, and I’m certain in the far future we’ll use ion drives to zip between Earth and Mars. I’m even sure some of them will even use solar power. They’ve been trying since 1971, but maybe [Ad Astra](https://web.archive.org/web/20170617195929/http://www.adastrarocket.com/aarc/) will finally [get somewhere with VASIMR afterall](https://web.archive.org/web/20170617195929/https://arstechnica.com/science/2017/02/nasas-longshot-bet-on-a-revolutionary-rocket-may-be-about-to-pay-off/). Maybe the [EM Drive will be completely validated and change everything](https://web.archive.org/web/20170617195929/https://en.wikipedia.org/wiki/RF_resonant_cavity_thruster). But don’t tell me we to **need** to pour billions more into solar electric propulsion research to get to Mars – chemical rockets have been getting things there just fine for decades.

In the meantime, Mars One was founded with the express purpose of permanently colonising Mars, and SpaceX was founded with the express purpose of establishing a sustained human presence on Mars too. Do you see either of them talking about needing further research into solar electric propulsion
No Just using conventional liquid rockets you say?

Funny that…
