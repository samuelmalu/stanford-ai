import util
import numpy as np
import matplotlib.pyplot as plt

np.seterr(all='raise')


factor = 2.0

class LinearModel(object):
  """Base class for linear models.

  Attributes:
    theta: np.ndarray, dtype=np.float64, shape=(n_features,). Weights vector for
      the model.
  """

  def __init__(self, theta=None):
    """
    Args:
      theta: (See class definition)
    """
    self.theta = theta

  def fit(self, x, y):
    """Fits the linear model to x -> y using np.linalg.solve.

    Remember to update self.theta with the fitted model parameters.

    Args:
      x: np.ndarray, dtype=np.float64, shape=(n_examples, n_features). Inputs.
      y: np.ndarray, dtype=np.float64, shape=(n_examples,). Outputs.

    Returns: Nothing

    Hint: use np.dot to support a vectorized solution
    """
    pass
    # *** START CODE HERE ***

    (n, k) = x.shape
    number_of_splits = n//k # split to ensure square input matrix
    
    for i in range(number_of_splits):
      loc_theta = np.linalg.solve(x[i:i+k], y[i:i+k])
      if(self.theta is None):
        self.theta = loc_theta
      else:
        # get loss
        loss = None
        self.theta = self.theta - loss

        self.theta =  np.dot(self.theta, loc_theta)

    # *** END CODE HERE ***

  def predict(self, x):
    """ Makes a prediction given a new set of input features.

    Args:
      x: np.ndarray, dtype=np.float64, shape=(n_examples, n_features). Model input.

    Returns: np.ndarray, dtype=np.float64, shape=(n_examples,). Model output.

    Hint: use np.dot to support a vectorized solution
    """
    pass
    # *** START CODE HERE ***
    return np.transpose(np.dot(self.theta, np.transpose(x)))
    # *** END CODE HERE ***

  @staticmethod
  def create_poly(k, x):
    """ Generates polynomial features of the input data x.

    Args:
      x: np.ndarray, dtype=np.float64, shape=(n_examples, 1). Training inputs.

    Returns: np.ndarray, dtype=np.float64, shape=(n_examples, k+1). Polynomial
      features of x with powers 0 to k (inclusive).
    """
    pass
    # *** START CODE HERE ***


    input_bases = list()

    for n in range(len(x)):
      input_bases.append(np.full((1, k+1), x[n]))
    input_bases = np.concatenate(input_bases) # n x k + 1
    powers = np.array([p for p in range(k + 1)]) # 1 x k+1
    input_poly = np.power(input_bases, powers)
    # print(x)
    # print(input_poly)
    return input_poly

    # *** END CODE HERE ***

  @staticmethod
  def create_sin(k, x):
    """ Generates sine and polynomial features of the input data x.

    Args:
      x: np.ndarray, dtype=np.float64, shape=(n_examples, 1). Training inputs.

    Returns: np.ndarray, dtype=np.float64, shape=(n_examples, k+2). Sine (column
      0) and polynomial (columns 1 to k+1) features of x with powers 0 to k
      (inclusive).
    """
    pass
    # *** START CODE HERE ***
    # *** END CODE HERE ***

def run_exp(train_path, sine=False, ks=[1, 2, 3, 5, 10, 20], filename='plot.png'):
  train_x,train_y=util.load_dataset(train_path,add_intercept=False)
  plot_x = np.ones([1000, 1])
  plot_x[:, 0] = np.linspace(-factor*np.pi, factor*np.pi, 1000)
  plt.figure()
  plt.scatter(train_x, train_y)

  for k in ks:
      '''
      Our objective is to train models and perform predictions on plot_x data
      '''
      # *** START CODE HERE ***
      model = LinearModel()
      x_featurized = model.create_poly(k, train_x)
      # print(f"x featurized: {x_featurized.shape}" )
      # print(f"train_y: {train_y.shape}" )
      model.fit(x_featurized, train_y)
      plot_x_featurized = model.create_poly(k, plot_x)
      plot_y = model.predict(plot_x_featurized)
      # *** END CODE HERE ***
      '''
      Here plot_y are the predictions of the linear model on the plot_x data
      '''
      plt.ylim(-2, 2)
      plt.plot(plot_x[:, 0], plot_y, label='k=%d' % k)

  plt.legend()
  plt.savefig(filename)
  plt.clf()


def main(train_path, small_path, eval_path):
  '''
  Run all experiments
  '''
  run_exp(train_path, True, [1, 2, 3, 5, 10, 20], 'large-sine.png')
  run_exp(train_path, False, [1, 2, 3, 5, 10, 20], 'large-poly.png')
  run_exp(small_path, True, [1, 2, 3, 5, 10, 20], 'small-sine.png')
  run_exp(small_path, False, [1, 2, 3, 5, 10, 20], 'small-poly.png')

if __name__ == '__main__':
  main(train_path='train.csv',
      small_path='small.csv',
      eval_path='test.csv')
