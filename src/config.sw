* Here there are the configuration file of the showmusic program.
* You can load a new configuration by using this file
*
* Intructions:
* Operations {
*   (rand) : generate a random note
*   (change_inst:midi_number) : change the default instrument
*   (play_note:note_number) : play the note
*   (silence:time) : time without sound
*   (octave:octave_number) : set the default octave
*   (silence:time) : time without sound (in secs)
*   (increase_volume:amount) : double the volume of the player
* }
*
*
* Variables{
*   $octave : actual default octave
*   $instrument : midi_value of the actual instrument
*   $
* }
*
*
* Every statment needs to be inside brackets []
* and it's only supported 1 command per line
* everything outside of the [] will be deleted so stick to the plan
*
* Example:

* aliases
tubular_bell = 131
Lá = (note:1)
Fá = (note:3)

[C -> (note:0)] * We are here mapping the char C  to the note:0
[C# -> Lá -> Fá]
[D -> (note:3)]
[D# -> (note:3)]
[E -> (note:4)]
[F -> (note:5)]
[F# -> (note:6)]
[G -> (note:7)]
[G# -> (note:8)]
[A -> (note:9)]
[A# -> (note:10)]
[B -> (note:11)]
[? -> (rand)]
[! -> (' ')]

* We don't support commands inside commands, so you can use
[[ -> (' ')], because the outer one will be counted
* this without problems
* but [] -> (rand)] is problematic

[\space -> (silence:0.5)]           * use this to represent spaces
[\tabs -> (silence:1)]              *tabs
[\n -> (instrument:tubular_bell)]   *new_line
