#!/usr/bin env lua

function printstr( strings , str )
   for i=1,str do
	  print(strings[i],#strings[i])
   end
end

strings = {}
strings[1] = "ACTG"
strings[2] = "ACGG"
strings[3] = "GGGT"


printstr( strings , 3 )


------------- PARTE 1: BRINCANDO COM A TABELA ----------------


function create_multidim_matrix( ndims, sizedims , matrix)
   for i=1,ndims do
	  matrix[i] = {}
	  for j=1,sizedims do
		 matrix[i][j] = 0
	  end
   end
end

matrix = {}
create_multidim_matrix( 3, 4, matrix )

for i=1,3 do
   for j=1,5 do -- no 5 vai ser nil
	  print(#matrix[i])
   end
end

------ PARTE 2: Criando matriz e imprimindo-a -----------

function LCSubstring(StrA, StrB)
   matrix = {}
   LCS = nil
   z = 0
   for i=1,#StrA do
	  matrix[i] = {}
	  for j=1,#StrB do
		 matrix[i][j] = 0
	  end
   end

   for i=1,#StrA do
	  for j=1,#StrB do
		 if StrA[i] == StrB[j] then
			if i== 1 or j == 1 then
			   matrix[i][j] = 1
			else
			   matrix[i][j] = matrix[i-1][i-1] + 1
			end
			if matrix[i][j] > z then
			   z = matrix[i][j]
			   LCS = string.sub(StrA,i-z+1,i)
			else
			   if matrix[i][j] == z then
				  LCS = string.sub(StrA,i-z+1,i)
			   end
			end
		else
		   matrix[i][j] = 0
		end
	  end
    end
    return LCS
end

print(LCSubstring("Batata","Atatab"))
