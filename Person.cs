public class Person
{
	public Person(PersonData data)
	{
		this.Name = data.Name;
		this.Gender = data.Gender;
	}

	public String Name {get; private set;}
	public String Gender {get; private set;}
}

public class PersonData
{
	public String Name;
	public String Gender;
}

public static Person ReadPerson(Reader reader)
{
	PersonData data = PersonData;
	data.Name = reader.ReadString();
	data.Gender = reader.ReadString();

	Person p = new Person(data)
	return p;
}