# XCS229-Handouts

This repository contains .tex and .pdf along with relevant files for Handouts used in XCS229: Machine Learning. Below is a snapshot of where each handout belongs within the scope of this class:

### XCS229: Machine Learning Handouts
- Supervised Learning
  - [Supervised Learning and Discriminative Algorithms](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Supervised%20Learning%20and%20Discriminative%20Algorithms.pdf) (Further reading: [Binary Classification and Logistic Regression](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Binary%20Classification%20and%20Logistic%20Regression.pdf), [Perceptron](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Perceptron.pdf))
  - [Generative Learning Algorithms](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Generative%20Learning%20Algorithms.pdf)
  - [Kernels and Support Vector Machines](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Kernels%20and%20Support%20Vector%20Machines.pdf) (Further Reading: [Representer Functions](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Representer%20Functions.pdf))
  - [Decision Trees](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Decision%20Trees.pdf) (Further Reading: [Boosting](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Boosting.pdf), [Ensemble Methods](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Ensemble%20Methods.pdf))
- Unsupervised Learning
  - [K-Means Clustering](https://github.com/scpd-proed/XCS229-Handouts/blob/main/K-Means%20Clustering.pdf)
  - [Mixture of Gaussians](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Mixture%20of%20Gaussians.pdf)
  - [Expectation Maximization Algorithm](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Expectation%20Maximization%20Algorithm.pdf)
  - [Factor Analysis](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Factor%20Analysis.pdf)
  - [Independent Component Analysis](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Independent%20Component%20Analysis.pdf)
  - [Principlal Component Analysis](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Principal%20Component%20Analysis.pdf)
- Deep Learning
  - [Deep Learning](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Deep%20Learning.pdf) (Further Reading: [Backpropagation](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Backpropagation.pdf))
- Learning Strategy
  - [Learning Theory](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Learning%20Theory.pdf) (Further Reading: [Bias-Variance](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Bias-Variance.pdf), [Error Analysis](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Error%20Analysis.pdf))
  - [Regularization and Model Selection](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Regularization%20and%20Model%20Selection.pdf)
- Reinforcement Learning
  - [Reinforcement Learning and Control](https://github.com/scpd-proed/XCS229-Handouts/blob/main/Reinforcement%20Learning%20and%20Control.pdf)
  - [LQR, DDP, and LQG](https://github.com/scpd-proed/XCS229-Handouts/blob/main/LQR,%20DDP,%20and%20LQG.pdf)

# Compiling Latex

Each subdirectory within this folder has, at a minimum, a file titled
`latexmkrc`.  This is the settings file for latexmk, which will handle
juggling the various latex engines preferred by the course staff.  A basic
`latexmkrc` file (e.g., for `pdflatex`) might have the following contents
([`latexmk` documentation](https://mirror.las.iastate.edu/tex-archive/support/latexmk/latexmk.pdf)):
```
@default_files = ("main.tex");   # Set the root tex file for the output document
$pdf_mode = 1;                   # tex -> PDF
$auto_rc_use = 1;                # Do not read further latexmkrc files
$warnings_as_errors = 1;         # Elevates warnings to errors.  Enforces cleaner code.
$pdflatex = "pdflatex -halt-on-error -interaction=batchmode %O %S";
                                 # Forces latexmk to stop and quit if it encounters an error
$jobname = "output_name";        # This is the name of the output PDF file
$silent = 1                      # For quieter output on the terminal.
```
Feel free to customize this as you desire, including adding more files,
directories, and media.  There is only one requirements:

**IT MUST BE POSSIBLE TO COMPILE EACH DOCUMENT USING ONLY THE FOLLOWING COMMAND:**
```
$ latexmk
```
A properly setup `latexmkrc` file can handle any special compilation options you
may require.  Put those options in the `latexmkrc` file so that other course
staff can compile your document with the command above.

Other commands that might be helpful include:
- `$ latexmk -pvc`:  (preview continuously) This will run `latexmk`
continuously, allowing you to immediately view changes to your output document
as you save source files.
- `$ latexmk -c`:  This will remove all auxiliary files other than the final
output PDF.
- `$ latexmk -C`:  This will remove all output files (including the final output
PDF).
