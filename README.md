## Dezvoltarea unui algoritm optimizat pe extensia DSP din Raspberry Pi pentru implementarea efectelor ecou și reverberație pe un fișier audio conținând voce

### Autori:

- Adam Iulian-Valentin
- Handaric Andrei

### Descriere proiect:

În implementarea acestui proiect, am dezvoltat un algoritm care prelucrează efectele de ecou și reverberație pe un fișier audio. Acest algoritm a fost optimizat în mai multe versiuni, până am obținut varianta cea mai eficientă din punct de vedere a timpului de execuție, varianta 4 sau finală. Pentru a compara peformanța algoritmului am analizat timpii de execuție pentru implementarea celor două efecte.

### Fișiere audio:

Pentru testarea algoritmului, am utilizat un sample din melodia Yiruma - River flows in you.

![Yiruma - River flows in you](yiruma.wav)

![Yiruma - River flows in you (echo)](yiruma_echo.wav)

![Yiruma - River flows in you (reverberation)](yiruma_reverberation.wav)

### Simularea timpului de execuție

![DSP_Runtime_V1](DSP_Runtime_V1.png)
![DSP_Runtime_V2](DSP_Runtime_V2.png)
![DSP_Runtime_V3](DSP_Runtime_V3.png)
![DSP_Runtime_V4](DSP_Runtime_V4.png)
