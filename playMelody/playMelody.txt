#include "pitches.h"
struct note {
  unsigned int frequency;
  unsigned long duration;
};

struct note melody[] = {
  //bad apple!!!
 { NOTE_AS5, 400 },
  //Aメロ
  { NOTE_DS5, 200 },
   { NOTE_F5, 200 },
   { NOTE_FS5, 200 },
    { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },

     { NOTE_DS6, 200 },
   { NOTE_CS6, 200 },
   { NOTE_AS5, 400 },
   { NOTE_DS5, 400 },

  { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
   { NOTE_FS5, 200 },
   { NOTE_F5, 200 },
   
    { NOTE_DS5, 200 },
   { NOTE_F5, 200 },
   { NOTE_FS5, 200 },
    { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },
     { NOTE_GS5, 200 },
   { NOTE_FS5, 200 },

 { NOTE_F5, 200 },
   { NOTE_DS5, 200 },
    { NOTE_F5, 200 },
     { NOTE_FS5, 200 },

      { NOTE_F5, 200 },
      { NOTE_DS5, 200 },
  { NOTE_D5, 200 },
  { NOTE_F5, 200 },

  //Aメロ2

{ NOTE_DS5, 200 },
   { NOTE_F5, 200 },
   { NOTE_FS5, 200 },
    { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },

     { NOTE_DS6, 200 },
   { NOTE_CS6, 200 },
   { NOTE_AS5, 400 },
   { NOTE_DS5, 400 },

  { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
   { NOTE_FS5, 200 },
   { NOTE_F5, 200 },
   
    { NOTE_DS5, 200 },
   { NOTE_F5, 200 },
   { NOTE_FS5, 200 },
    { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },
     { NOTE_GS5, 200 },
   { NOTE_FS5, 200 },

{ NOTE_F5, 400 },
{ NOTE_FS5, 400 },
{ NOTE_GS5, 400 },
{ NOTE_AS5, 400 },



//Bme
 { NOTE_CS6, 200 },
   { NOTE_DS6, 200 },
   { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },

{ NOTE_GS5, 200 },
{ NOTE_AS5, 200 },
{ NOTE_CS6, 200 },
   { NOTE_DS6, 200 },
   { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },

{ NOTE_GS5, 200 },
{ NOTE_AS5, 200 },
{ NOTE_GS5, 200 },
{ NOTE_FS5, 200 },
{ NOTE_F5, 200 },
{ NOTE_CS5, 200 },
{ NOTE_DS5, 400 },

{ NOTE_CS5, 200 },
{ NOTE_DS5, 200 },
{ NOTE_F5, 200 },
{ NOTE_FS5, 200 },
{ NOTE_GS5, 200 },
{ NOTE_AS5, 200 },
{ NOTE_DS5, 400 },

//二回目
{ NOTE_AS5, 200 },
{ NOTE_CS6, 200 },
 { NOTE_CS6, 200 },
   { NOTE_DS6, 200 },
   { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },

{ NOTE_GS5, 200 },
{ NOTE_AS5, 200 },
{ NOTE_CS6, 200 },
   { NOTE_DS6, 200 },
   { NOTE_AS5, 200 },
   { NOTE_GS5, 200 },
    { NOTE_AS5, 400 },


{ NOTE_DS6, 200 },
{ NOTE_F6, 200 },
{ NOTE_FS6, 200 },
{ NOTE_F6, 200 },
{ NOTE_DS6, 200 },
{ NOTE_CS6, 200 },
{ NOTE_AS5, 400 },
{ NOTE_GS5, 200 },
{ NOTE_AS5, 200 },


{ NOTE_GS5, 200 },
{ NOTE_FS5, 200 },
{ NOTE_F5, 200 },
{ NOTE_CS5, 200 },
{ NOTE_DS5, 400 }
};

void setup() {
  pinMode(2, OUTPUT);
  int melody_length = sizeof(melody) / sizeof(melody[0]);

    for (int thisNote = 0; thisNote < melody_length; thisNote++) {
    tone(2, melody[thisNote].frequency);

    delay(melody[thisNote].duration);
  }
  noTone(2);
}
void loop(){

}