파일 업로드 다운로드를 책임지는 도메인

api : controller 클래스가 존재합니다. 해당 프로젝트에서 스프링 부트는 Rest API 서버로서의 역할만을 하기 때문에, 명시적으로 api라는 네이밍으로 패키징 했습니다.
application : 주로 service 클래스들이 존재합니다. DB 트랜잭션이 일어나며, 주된 비즈니스 로직을 담당합니다. Service 클래스들 뿐만 아니라, handler와 같은 같은 성격의 다른 클래스 또한 포함하기 때문에 application이라는 네이밍으로 패키징 했습니다.
dao : dao, repository 클래스들로 구성됩니다.
domain : entity 클래스들로 구성됩니다.
dto : dto 클래스들로 구성됩니다.
exception : exception 클래스들로 구성됩니다.