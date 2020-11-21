* Here there are the configuration file of the showmusic program.
* You can load a new configuration by using this file
*
* Intructions:
* Operations {
*   (rand) : generate a random note
*   (instrument:'midi_number') : change the default instrument
*   (note:'note_number') : play the note
*   (silence:'time') : time without sound
*   (octave:'octave_number') : set the default octave
*   (silence:'time') : time without sound (in secs)
*   (volume:raise 'amount') : raise by 1 the volume of the player
* }

* Rand
* (rand 'min' 'max')
* default value are 0,127

* Instruments, Octaves, Volume and Bpm have:
* (raise 'amount')
* (double)
* (lower 'amount')
* (half)

* Every statment needs to be inside brackets []
* and it's only supported 1 command per line
* Example:

* Aliases:

* Aliases only work for full commands,
* trying to use SomeInstrument = 123 will not work

* There is some variables that are already set:

* $vowels = "all the minuscle vowels", that will create a
* command for all the minuscle vowels

* $VOWELS = "all the maiscle vowels"

* $number = "digits in general", they can be passed as argument for
* some of the commands that accepts numbers

TubularBells = 131
Agogo        = 114
PanFlute     = 76
Harpsichord  = 7
ChurchOrgan  = 20

Dó   = (note:72)
Ré   = (note:74)
Mi   = (note:76)
Fá   = (note:77)
Sol  = (note:79)
Lá   = (note:81)
Si   = (note:83)

* Mapping

[C  -> Dó]
[D  -> Ré]
[E  -> Mi]
[F  -> Fá]
[G  -> Sol]
[A  -> Lá]
[B  -> Si]

[a -> (repeat)]
[b -> (repeat)]
[c -> (repeat)]
[d -> (repeat)]
[e -> (repeat)]
[f -> (repeat)]
[g -> (repeat)]

[i -> (instrument:Harpsichord)]
[o -> (instrument:Harpsichord)]
[u -> (instrument:Harpsichord)]
[I -> (instrument:Harpsichord)]
[O -> (instrument:Harpsichord)]
[U -> (instrument:Harpsichord)]

[?  -> (octave:raise 1)]
[;  -> (instrument:PanFlute)]
[,  -> (insturment:ChuchOrgan)]
[!  -> (instrument:Agogo)]

[\space -> (volume:raise 1)]
[\default -> (repeat)]
[\newline -> (instrument:TubularBells)]

[$number -> (instrument:raise $number)]
* We 'only' have 128 instruments, rising above that will go back to
* number 1


* We don't support commands inside commands, so you can use
* [[ -> (repeat)] for example, because the outer one will be counted
* but [] -> (rand)] is problematic
* I don't believe that you will need this '[' ']' so don't use it please
