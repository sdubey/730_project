from mr_word_freq_count import MRWordFreqCount
from runJob import runJob


def trend(input_file, output_dir):
	runJob(MRWordFreqCount, input_file, output_dir)
