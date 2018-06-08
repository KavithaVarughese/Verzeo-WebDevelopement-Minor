	
	var Employee = new Object;	
	
		function display()
		{
			document.getElementById('disname').innerHTML = 
				document.getElementById('name').value
			document.getElementById('disage').innerHTML = 
				document.getElementById('age').value
			document.getElementById('dissal').innerHTML = 
				document.getElementById('sal').value
			document.getElementById('disdes').innerHTML = 
				document.getElementById('des').value
		}
		function checkcomp()
		{
			if(checksal() && checkage())
			{
			var canc = document.getElementById('canc')
			var con = document.getElementById('conf')
			con.style.visibility = "visible";
			canc.style.visibility = "visible";
			}
			display();
			
		}

		function store()
		{
			Employee.name = document.getElementById('name').value
			Employee.age = document.getElementById('age').value
			Employee.salary = document.getElementById('sal').value
			Employee.designation = document.getElementById('des').value
			disp()
		}

		function rel()
		{
			document.location.reload();
		}

		function checkage()
		{
			if(isNaN(parseInt(document.getElementById('age').value)))
			{
				alert("please enter a number for age")
				return false;
			}
			return true;
		}
			function checksal()
		{
			if(isNaN(parseInt(document.getElementById('sal').value)))
				{
					alert("please enter a number for salary")
					return false;
				}
				return true;
		}

		function disp()
		{
			document.write("Name : " + Employee.name + "<br>")
			document.write("Age : " + Employee.age + "<br>")
			document.write("Salary : " + Employee.salary + "<br>")
			document.write("Designation : " + Employee.designation + "<br>")
		}