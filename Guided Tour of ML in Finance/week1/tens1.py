import numpy as np
import os

import matplotlib
import matplotlib.pyplot as plt

import time

def reset_graph(seed=42):
    tf.reset_default_graph
    tf.set_random_seed(seed)
    np.random.seed(seed)

import tensorflow as tf

reset_graph()

x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
a = tf.constant(2, name='a')

print(x.graph is tf.get_default_graph())
print(y.graph is tf.get_default_graph())
print(a.graph is tf.get_default_graph())


graph = tf.Graph()
with graph.as_default():
    x2 = tf.Variable(2)

print(x2.graph is graph)
print(x2.graph is tf.get_default_graph())

#variables or constants are not yet initalized
x,y,a

# Now define function f(x,y) = x^2 + y + a
f = x*x*y+y+a

# lazy evaluation
f

#to evaluate the graph, we open a tensorflow session
#A tf session initializes all variables and evaluate the graph. It puts graph operations on a CPU or GPU and holds all the variable values
sess = tf.Session()
sess.run(x.initializer)
sess.run(y.initializer)
#constant needs not be inialized
result = sess.run(f)
a_val = a.eval(session=sess)
print('a=', a_val)
print('result=',result)
sess.close()

#run a session with automatic closing at the end
with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    result = f.eval()   # same as sess.run(f)
    a_val = a.eval()

print('a=', a_val)
print('result=', result)


#initialization of all variables at once
init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run()
    result = f.eval()

print(result)

init

#lifecycle of a node value
w = tf.constant(3)
x = w+2
y = x+5
z = x*3

#in this example, code evaluates w and x twice:
with tf.Session() as sess:
    print(y.eval())
    print(z.eval())

#all node values are dropped between runs, except variable values
# a variable starts it life when its initalizer is run, and ends it when the session is closed
print(x)

#in this example the evaluation of w and x is only done once:
with tf.Session() as sess:
    y_val, z_val = sess.run([y,z])
    print(y_val)
    print(z_val)


#define a composite function f(w) = exp(w20+w21X(exp(w10+w11Xexp(w00+w01Xx)))

#implement in tf
def my_func(w,x):
    f_0 = tf.exp(w[0,0] + w[0,1]*x)         #the inner-most function
    f_1 = tf.exp(w[1, 0] + w[1, 1] * f_0)     #the next-level function
    f_2 = tf.exp(w[2, 0] + w[2, 1] * f_1)     #the output function

    return f_2, f_1, f_0

#fancier implementation using name scopes:
def my_func2(w,x):
    with tf.name_scope("f_0_level") as scope_0:
        f_0 = tf.exp(w[0,0] + w[0,1]*x)
    with tf.name_scope("f_1_level") as scope_1:
        f_1 = tf.exp(w[1,0] + w[1,1]*f_0)
    with tf.name_scope("f_2_level") as scope_2:
        f_2 = tf.exp(w[2,0] + w[2,1]*f_1)
    return f_2, f_1, f_0


#w_0 is a point at which we want to compute the function and its derivatives
#w_0 = np.random.rand(3,2)
w_0 = np.vstack((np.zeros(3), np.ones(3))).T
print(w_0)

# a manual check of derivatives at w = w0:
# df/dw20 = df/wf2 = f2(w0), ...
# compute graidents using TF

reset_graph()
w = tf.Variable(w_0, name='w', dtype=tf.float32)
x = tf.Variable(1.0, name='x', dtype=tf.float32, trainable=False)
f_2, f_1, f_0 = my_func2(w,x)
grads = tf.gradients(f_2, w)
print(grads)


# a node for the initializer
init = tf.global_variables_initializer()

#run the session
t_0 = time.time()
with tf.Session() as sess:
    sess.run(init)

    #function_vals = sess.run([f_2,f_1, f_0])
    #gradients = sess.run(grads)
    gradients, function_vals = sess.run([grads, [f_2, f_1, f_0]])
print("computed derivatives in %f3.2 sec" % (time.time() - t_0))
print("funcation values = ", function_vals)
print("gradients=", gradients)

#function is reinitalized and resetted and empty
print(my_func2(w_0, x))

from IPython.display import clear_output, Image, display, HTML

def strip_consts(graph_def, max_const_size = 32):
    strip_def = tf.GraphDef()
    for n0 in graph_def.node:
        n = strip_def.node.add()
        n.MergeFrom(n0)
        if n.op == 'Const':
            tensor = n.attr['value'].tensor
            size = len(tensor.tensor_content)
            if size > max_const_size:
                tensor.tensor_content = b"<stripped %d bytes>"%size
            return strip_def
def show_graph(graph_def, max_const_size=32):
    """visualize TensorFlow graph."""
    if hasattr(graph_def, 'as_graph_def'):
        graph_def = graph_def.as_graph_def()
        strip_def = strip_consts(graph_def, max_const_size=max_const_size)
        code = """
        <script>
        function load() {{
            document.getElementById("{id}").pbtxt = {data};
            }}
        </script>
        <link rel="import" href="https://tensorboard.appspot.com/tf-graph-basic.build.html" onload=load()>
        <div style="height:600px">
            <tf-graph-basic id="{id}"></tf-graph-basic>
        </div>
        """.format(data=repr(str(strip_def)), id='graph'+str(np.random.rand()))

        iframe = """
            <iframe seamless style="width:1200px;height:620px; border:0" srcdoc ="{}"></iframe>
        """.format(code.replace('"', '&quot;'))
        display(HTML(iframe))

show_graph(tf.get_default_graph())

