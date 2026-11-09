---
name: plain-talk
description: Use before writing anything a person will read and act on - a status update, a question to a user or client, an error message, a ticket, a pull request description, a review finding, a handover note or a message to another agent.
---

# Plain talk

The reader sees your message on its own, often hours later, without the context you have. Write so it
makes sense by itself.

## The six rules

1. **Main thing first.** The first sentence says what happened or what you need. Detail comes after, if
   it is needed at all.
2. **One point per message.** One question per message. One topic per paragraph. At most four sentences
   in a paragraph.
3. **Short sentences, plain words.** Keep a sentence under 20 words. Prefer the shorter word. Name
   things by what they are ("the login fix"), not by an identifier the reader has to look up. Where an
   identifier is needed, say what it is the first time: "#1027 (the login fix)".
4. **Facts, not feelings.** No "I think", "it seems", "unfortunately", "great news". No exclamation
   marks. No "just", "simply", "easy", "quick". Apologise once, and only for your own mistake.
5. **A question works on its own.** Name the thing and the choice, and say what happens if nobody
   answers: "The new report page passed review. Publish it now, or wait for the client's logo? It stays
   unpublished until you choose."
6. **An error says what failed and what to do.** "The upload was refused: the file is over 20 MB.
   Compress it or split it, then upload again." Not the log, not the rule text, not a code alone.

## Shapes

| Writing | Shape |
| --- | --- |
| **Status update** | What happened, what you did, what you need. Two to four sentences. Long evidence goes in an attachment or link, with one line saying what it shows |
| **Question to a decision-maker** | Title saying what the decision is about; two or three sentences of context (what this is, why now, what happens with no decision); one question ending in "?"; two to four options, each an action and its consequence; your recommendation and why |
| **Ticket** | Outcome (what is true when done, measurable); why (the evidence); what to change; done when (a checklist) |
| **Review finding** | Where; what goes wrong and when; the fix. One finding per entry. Severity stated separately from the description |
| **Pull request description** | What changed (two sentences); why (one paragraph); what was left out and why; what was checked; security (one line if nothing changed) |
| **Handover or run report** | Done, not done, next. Then the evidence |

A list for options or steps. Prose for one idea.

## Words

| Use | Instead of |
| --- | --- |
| stop, end, cancel | kill, abort, terminate |
| ask, tell | escalate, surface, flag |
| turn on, turn off | enable, disable |
| might | may (when you mean "possibly") |
| to | in order to |
| lets you | allows you to |
| the server refused the upload | the upload errored out |
| the test `name` failed | the suite exhibited a failure |
| Monday 3 November, 14:00 UK | tomorrow, currently, later |

- Say "you" to the reader.
- One name for one thing, all the way through.
- No internal state names. Say what the state means: "waiting for a review".
- Present tense for state: "Review done", not "Review has been completed".
- Say who did what: "the reviewer found two problems", not "two problems were found".

## Between agents

A message from one agent to another is read by a model. The same rules apply, shorter: drop every
pleasantry, hedge and filler word. Keep full sentences, exact names, exact error text and the order of
steps. Do not drop articles or joining words; that can change which step comes first.

**Before:** "Hi, just wanted to let you know that I think the tests might be failing because of the
lock, could you possibly take a look when you get a chance?"

**After:** "Tests on commit 80001f8 are waiting for the test lock held by the other build. Nothing
needed. Next report in 20 minutes."

## Before sending

- [ ] The first sentence says what happened.
- [ ] Someone who sees only this message can act on it.
- [ ] At most one question, with what happens if it goes unanswered.
- [ ] No sentence of 20 words or more. Count them; ignore code and identifiers.
- [ ] No paragraph over four sentences.
- [ ] No hedge, hype, exclamation mark or second apology.
- [ ] Every identifier is explained the first time, or removed.

## Example

**Before:** "I've answered the planner's questions on the queue work and it's writing the plan now.
The three developers are still held up by the push check, and I'm waiting on someone to look at the
test records. Nothing new since my last update, and nothing needs a decision from you."

**After:** "No decision needed. The planner is writing the plan for the queue work. Three developers
cannot push until their test records are checked."

## Sources

Google's People + AI Guidebook, Google's conversation design guidance, the Google developer
documentation style guide, and Material Design's writing guidance. Google allows 26 words a sentence;
this skill uses 20 because most of these messages are read on a small card or in a notification.
