
import sox
import matplotlib.pyplot as plt

audio_file = 'pedro-pedro-pe.mp3'
tfm = sox.Transformer()

array_out = tfm.build_array(input_filepath=audio_file)

# print(array_out.max())

# Créer un graphique
plt.figure(figsize=(10, 4))
plt.plot(array_out)
plt.title('Données audio')
plt.xlabel('Temps (échantillons)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()