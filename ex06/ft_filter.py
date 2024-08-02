def ft_filter(function, iterable):
  '''Filtra elementos de un iterable.

  Args:
    function: Una función que devuelve un valor booleano.
    iterable: Un objeto iterable.

  Returns:
    Una lista de elementos para los que la función devolvió True.
  '''
  return [item for item in iterable if function(item)]
