import numpy as np
import mne

sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file, preload=True)

#print(raw)
#print(raw.info)

raw.compute_psd(fmax=50).plot(picks="data", exclude="bads")
raw.plot(duration=50, n_channels=30, block=True)

# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these are omitted here
ica.plot_properties(raw, picks=ica.exclude)