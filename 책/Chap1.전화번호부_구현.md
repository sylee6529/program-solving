### 전화번호부 검색 기능 작성해보기

```
public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String phoneNumber = in.nextLine();
}
```

- 전화번호는 어떤 형식으로 나타낼 것인가
- 전화번호부에 저장되어 있는 사람은 어떻게 나타낼 것인지
- 사람과 전화번호는 어떻게 비교할 것인지
- 전화번호부는 어떤 형식으로 나타낼 것인지

1. 전화번호 나타내기

```java
phoneNumber.replaceAll("[^0-9]", "");
```

```java
private static class PhoneNumber {
	public final String phoneNumber;
	
	public PhoneNumber(String rawPhonePhoneNumber) {
		this.phoneNumber = rawPhoneNumber.replaceAll("[^0-9]", "");
	}
}
```

```java
@Override
public String toString() {
	return "PhoneNumber{" +
		"phoneNumber='\'" + phoneNumber + "\'" + "}";
}
```

➖메인 메소드 내용

```java
public static void main(String[] args) {
	System.out.println(new PhoneNumber("010-1234-5678");
	Systetm.out.println(new PhoneNumber("010 1234 5678");
}
```

1. 전화번호부의 사람 나타내기

```java
private static class Person {
	public final String name;
	private final List<PhoneNumber> numbers;
	
	public Person(String name) {
		this.name = name;
		numbers = new ArrayList<>();
	}
	
	public boolean addPhoneNumber(PhoneNumber number) {
		for (char c : number.toCharArray()) {
			if(!Character.isDigit(c))
				return false;
		}
		numbers.add(number);
		return true;
	}
}
```

- 한번 값이 정해진 이후에 값이 변경되지 않는 것은 final을 붙여 값 변경 방지.
- 외부에서 접근하여 변경 가능한 변수는 private 선언
- String처럼 값이 불변인 객체는 읽기만 가능하므로 public으로 선언한다.

➖ 메인 메소드 내용

```java
public static void main(String[] args) {
	Person person = new Person("홍길동");
	person.addPhoneNumber(new PhoneNumber("010-1234-5678"));
	person.addPhoneNumber(new PhoneNumber("010 1234 4678"));
	System.out.println(person);
}
```

1. 사람과 전화번호 비교하기

<aside>
💡 **String 배열에 특정 String이 존재하는지 비교할 때, contains 조심** 
`리스트.contains` 는 `equals()` 메서드를 사용하여 객체를 비교한다.
equals() 메서드는 별도의 오버라이딩이 없으면 객체가 같을 때만 true를 반환한다. (서로 다른 두 객체를 비교하게 되면 false가 반환됨)

</aside>

```java
private static class Person {
	//...
	public boolean hasPhoneNumber(PhoneNumber number) {
		// return numbers.contains(number);   // 이렇게 하면 의도대로 동작X
		
	}
	
	@Override
	public boolean equals(Object o) {
		if(!o instanceof PhoneNumber)) return false;
		return phoneNumber.equals(((PhoneNumber) o).phoneNumber);
	}
}
```

1. 전화번호부 나타내기

```java
public static class PhoneBook {
	private final List<Person> people;
	
	private PhoneBook() {
		people = new ArrayList<>();
	}
	
	public void addPerson(Person person) {
		people.add(person);
	}
}
```

➖ 메인 메소드 내용

```java
public static void main(String[] args) {
	Person person1 = new Person("홍길동");
	person.addPhoneNumber(new PhoneNumber("010-1234-5678"));
	person.addPhoneNumber(new PhoneNumber("010 3456 4678"));
	
	Person person2 = new Person("김철수");
	person.addPhoneNumber(new PhoneNumber("010-4235-5678"));
	
	Person person3 = new Person("이영희");
	person.addPhoneNumber(new PhoneNumber("010-3535-5678"))
	
	PhoneBook phoneBook = new PhoneBook();
	phoneBook.addPerson(person1);
	phoneBook.addPerson(person2);
	
	System.out.println(phoneBook);
}
```

⚠️ **문제점: 전화번호부에 같은 객체가 여러번 추가된다 → List 대신 Set 사용**

```java
public static class PhoneBook {
	private final Set<Person> people;
	
	private PhoneBook() {
		people = new HashSet<>();
	}
	
	public void addPerson(Person person) {
		people.add(person);
	}
}
```

전화번호로 Person을 찾는 메서드 구현하기

```java
public search(PhoneNumber number) {
	return people.stream()
		.filter(p -> p.hasPhoneNumber(number))
		.findFirst()
		.orElse(null);
}
```

- `people.stream()`: `Set<Person>` → `Stream<Person>`
- `filter()`: number를 가지는 Person 객체 탐색
- `findFirst()`: number를 갖는 Person 객체가 있는지 검사
- `orElse()`: 없다면 null 반환

➖ 메인 메소드 내용

```java
public static void main(String[] args) {
	//...
	System.out.println(phoneBook.search(new PhoneNumber("010-1234-5678")));
}
```