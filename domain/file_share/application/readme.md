application 디렉터리는 도메인 객체와 외부 영역을 연결해주는 파사드와 같은 역할을 주로 담당하는 클래스로 구성됩니다.
대표적으로 데이터베이스 트랜잭션을 처리를 진행합니다.

> GRASP 원칙: Controller, Low Coupling, High Cohesion \
Controller 원칙에 따라 시스템의 흐름을 제어하고 요청을 처리합니다. repository 의 interface 를 사용하기 때문에 Low Coupling을 통해 외부 시스템과의 결합도를 낮추고, High Cohesion을 통해 도메인 로직과 관련된 작업을 처리합니다.