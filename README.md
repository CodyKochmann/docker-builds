# Docker Builds

This is a collection of helpful containers I've used for a variety of different projects. 

If I find myself needing something with a specific setup multiple times, it becomes a build that is added here for future usage.

Some of the builds are not very complex. Sometimes it's just tweaking a default behavior to make the tool easier to use. Other times it's an overhaul of the default configuration to optimize a bloated system for more reliable and lighter weight setups.

#### Note about the approach of the tweaks:

These are opinionated builds. In my opinion stability, lightness and debuggability are prerequisites to speed, not afterthoughts.

If we want more speed and truly can't reduce the application's workload any more, going horizontal is easy because the work was put in to minimize each components' requirements.

#### Do not scale bloated applications. 

Here's the steps I took to remove quite a bit of the bloat in these builds.

1. Read the manual. 
2. Defaults tend to overcompensate to allow people who don't care or have time for the details to use the system. Never judge a system based on its defaults.
3. If the two previous steps didn't work. Figure out what part of the bloat is just the application re-inventing something that would be given to us for free from the kernel.
