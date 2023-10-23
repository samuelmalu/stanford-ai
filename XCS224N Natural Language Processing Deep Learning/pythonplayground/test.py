
window = 4
corpus_segment = ["a", "b", "c", "d","a", "g", "k"]
index = 1;
left_index = max(0, index - window)
left_window = corpus_segment[left_index:index]

right_index = min(len(corpus_segment), index + window + 1)
right_window = corpus_segment[index + 1: right_index];

window = left_window + right_window;

print(left_window)
print(right_window)
print(window)