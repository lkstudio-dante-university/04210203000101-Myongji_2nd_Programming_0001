using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * 구조체란?
 * - 사용자 정의 자료형 중 하나로서 변수 및 메서드를 하나의 그룹으로 관리 할 수 있는 기능을 의미한다. (즉, 구조체를 활용하면
 * 관련 된 데이터와 메서드를 하나의 데이터로 관리하는 것이 가능하다.)
 * 
 * 구조체는 값 형식 자료형이기 때문에 해당 자료형으로 선언 된 변수를 다른 변수에 할당하면 완전한 사본이 만들어진다는 특징이
 * 존재한다.
 * 
 * C# 구조체 선언 방법
 * - struct + 구조체 이름 + 구조체 멤버 (변수, 메서드 등등...)
 * 
 * Ex)
 * struct STData {
 *     public int m_nVal;
 *     public float m_fVal;
 * }
 */
namespace E01 {
	/*
	 * 접근 제어 지시자 (한정자) 란?
	 * - 구조체 또는 클래스가 지니고 있는 멤버를 보호하기 위한 보호 수준을 의미한다. (즉, 명시 된 접근 제어 지시자에 따라
	 * 특정 멤버에 접근이 불가능 할 수 있다는 것을 알 수 있다.)
	 * 
	 * C# 접근 제어 지시자 종류
	 * - public			<- 내/외부에서 모두 접근 가능
	 * - protected		<- 클래스 내부 및 자식 클래스에서 접근 가능
	 * - private		<- 클래스 내부에서 접근 가능
	 */
	/** 데이터 */
	public struct STE06Data {
		public int m_nVal;
		public float m_fVal;

		/*
		 * 생성자란?
		 * - 구조체 또는 클래스를 통해 생성 된 데이터를 초기화하기 위한 특별한 메서드를 의미한다. (즉, 생성자는 구조체 및
		 * 클래스 이외에는 사용하는 것이 불가능하다는 것을 알 수 있다.)
		 * 
		 * 생성자는 일반적인 메서드와 달리 직접적으로 호출하는 것이 불가능하며 C# 컴파일러에 의해서 자동으로 호출되는 특징이
		 * 존재한다.
		 */
		/** 생성자 */
		public STE06Data(int a_nVal, float a_fVal) {
			m_nVal = a_nVal;
			m_fVal = a_fVal;
		}
	}

	/** Example 6 */
	public partial class CE01Example_06 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_06;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

			/*
			 * new 키워드를 활용하면 구조체 데이터를 생성하는 것이 가능하다. (즉, 해당 키워드로 구조체를 생성하면 내부적으로
			 * 해당 구조체의 생성자가 호출된다는 것을 알 수 있다.)
			 * 
			 * var 키워드란?
			 * - 자동으로 변수의 자료형을 지정해주는 키워드를 의마한다. (즉, 해당 키워드를 활용하면 변수의 자료형을 자동으로
			 * 설정해줌으로서 변수 선언 명령문을 좀 더 수월하게 작성하는 것이 가능하다.)
			 * 
			 * 단, 해당 키워드를 통해서 선언 된 변수는 반드시 초기화 값을 명시해줘야한다. (즉, C# 컴파일러는 초기화 값의
			 * 자료형을 기반으로 해당 변수의 자료형을 지정한다는 것을 알 수 있다.)
			 */
			var stData = new STE06Data(10, 3.14f);

			Debug.Log("=====> 구조체 <=====");
			Debug.Log($"정수 : {stData.m_nVal}");
			Debug.Log($"정수 : {stData.m_fVal}");
		}
		#endregion // 함수
	}
}
