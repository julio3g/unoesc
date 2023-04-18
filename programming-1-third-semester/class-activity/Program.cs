using AttClasses.Classes;

Person[] people = new Person[]
{
    //GERENTE
    new userWorker{
        Name = "José"
        , Office = "Gerente"
        , BirthDate = new DateTime(1989, 8, 23)
        , Gender = "Masculino"
        , Sector = "Geral"
        , Contract = new DateTime(2008, 2, 1)
        , Salary = 8000.50m
    },

    //SUPERVISOR
    new userSupervisor{
        Name = "Ana"
        , Office = "Supervisor"
        , BirthDate = new DateTime(1992, 7, 30)
        , Gender = "Feminino"
        , Sector = "T.I"
        , Contract = new DateTime(2010, 7, 21)
        , Period = "Noturno"
    },

    new userSupervisor{
        Name = "Gabriel"
        , Office = "Supervisor"
        , BirthDate = new DateTime(1994, 6, 12)
        , Gender = "Masculino"
        , Sector = "T.I"
        , Contract = new DateTime(2011, 5, 8)
        , Period = "Diurno"
    },

    //OPERARIO
    new userWorker{
        Name = "João"
        , Office = "Funcionário"
        , BirthDate = new DateTime(2003, 2, 20)
        , Gender = "Masculino"
        , Sector = "T.I"
        , Contract = new DateTime(2019, 3, 5)
        , Function = "Manutenção"
    },
    new userWorker{
        Name = "Julia"
        , Office = "Funcionário"
        , BirthDate = new DateTime(2004, 5, 14)
        , Gender = "Masculino"
        , Sector = "T.I"
        , Contract = new DateTime(2017, 2, 5)
        , Function = "Sistemas"
    },
    new userWorker{
        Name = "Maria"
        , Office = "Funcionário"
        , BirthDate = new DateTime(1996, 3, 30)
        , Gender = "Feminino"
        , Sector = "Recepção"
        , Contract = new DateTime(2017, 3, 18)
        , Function = "Recepcionista"
    }


};

for(int i = 0; i < people.Length; i++)
{
   Console.WriteLine($"Pessoa {i + 1}:");
   Console.WriteLine($"Name: {people[i].Name}" + $" / Office: {people[i].Office}");

   Console.WriteLine($"Data de BirthDate: {people[i].BirthDate.ToShortDateString()}");
   Console.WriteLine($"Data de contratação: {people[i].Contract.ToShortDateString()}");
   Console.WriteLine($"Gênero: {people[i].Gender}");
   Console.WriteLine($"Sector: {people[i].Sector}");


   if(people[i] is userWorker)
   {
    userWorker manager = (userWorker)people[i];
    Console.WriteLine($"Salário: {manager.Salary}");
   }
   else if (people[i] is userSupervisor)
   {
    userSupervisor supervisor = (userSupervisor)people[i];
    Console.WriteLine($"Período de trabalho: {supervisor.Period}");
   }
   else if (people[i] is userWorker)
   {
    userWorker operario = (userWorker)people[i];
    Console.WriteLine($"Função: {operario.Function}");
   }

   Console.WriteLine();
}
