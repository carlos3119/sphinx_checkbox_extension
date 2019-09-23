# sphinx_checkbox_extension
A simple extension that allows to use Checkboxes in Sphinx Doc

Using this (https://www.sphinx-doc.org/en/master/development/tutorials/todo.html) tutorial as starting point, I created an Extension for Sphinx that allows us to use HMTL checkboxes for the HTML documentation generation. 

# Requisites : 
- Python : https://www.python.org/downloads/ 
    used 3.7.3
- Sphinx : http://www.sphinx-doc.org/en/master/usage/installation.html
    used 2.2.0


# Usage :
- Start a sphinx project (https://sphinx-tutorial.readthedocs.io/start/)

- Configure source/conf.py :
    - Include path to our extensions : 
        sys.path.append(os.path.abspath("./_ext"))
        
    - Include checkbox extension : 
        include_checkbox = True
    
- Take a look at *source/_ext/checkbox.py*
    
- Use **checkboxes** in your rst file :
      
      <... your docu ...>
    
      .. checkbox:: Item 1 : should be checked
          :checked: yes
      .. checkbox:: Item 2 : should be unchecked
          :checked: no
      .. checkbox:: Item 3 : should be unchecked by default

      <... your docu continues ...>
