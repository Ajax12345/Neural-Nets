#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iomanip>
#include <cmath>

using namespace std;

struct Brain
{
  double w = 0.4;
  double a = 0.01;
  double E = 0.4;
  void activation(vector<int>&x, int y)
  {
    double summed_input = 0;
    for (int i = 0; i < x.size(); i++)
    {
      summed_input += summation(x[i]);

    }
    double output = sigma(summed_input);
    double E = error(y, output);
    delta_w(E, output, x);

  }
  double summation(int x)
  {
    return w*(double)x;
  }
  double sigma(int z)
  {
    return 1/(1+pow(2.7181, -z));
  }
  double error(int target, double the_output)
  {
    return 0.5*(pow((double)target-the_output, 2));
  }
  void delta_w(double E, double new_output, vector<int>&the_input)
  {
    double sum = 0.0;
    for (int i = 0; i < the_input.size(); i++)
    {
      sum += summation(the_input[i]);
    }
    w += a*new_output*(1-new_output);

  }
  void new_input(vector<int>&x)
  {
    double the_sum = 0.0;
    for (int i = 0; i < x.size(); i++)
    {
      the_sum += summation(x[i]);
    }

    double final_output = sigma(the_sum);
    cout << final_output<< endl;
  }


};
int main()
{


  ifstream input;
  input.open("prediction_data.txt");
  int a, b, c;
  string type;
  vector<vector<int> >input_numbers;
  vector<int>input_type;

  while (!input.eof())
  {
    vector<int>interior_data;
    input >> a >> b >> c;
    cout << a << " "<< b << " "<< c << endl;
    interior_data.push_back(a);
    interior_data.push_back(b);
    input_type.push_back(c);
    input_numbers.push_back(interior_data);

    interior_data.clear();

  }


  Brain the_brain;
  for (int i = 0; i < input_type.size(); i++)
  {
    the_brain.activation(input_numbers[i], input_type[i]);

  }
  vector<int>other_data = {0, 1};
  the_brain.new_input(other_data);

  input.close();
}
