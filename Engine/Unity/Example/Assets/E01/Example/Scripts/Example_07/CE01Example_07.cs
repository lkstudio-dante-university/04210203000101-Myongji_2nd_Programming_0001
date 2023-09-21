using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
 * 클래스란?
 * - 사용자 정의 자료형 중 하나로서 변수 및 메서드를 하나의 그룹으로 관리 할 수 있는 기능을 의미한다. (즉, 클래스를 활용하면
 * 관련 된 데이터와 메서드를 하나의 데이터로 관리하는 것이 가능하다.)
 * 
 * 클래스는 참조 형식 자료형이기 때문에 해당 자료형으로 선언 된 변수를 다른 변수에 할당하면 얕은 복사가 발생한다는 것을 알 수
 * 있다.
 * 
 * 클래스는 구조체와 달리 상속 및 다형성을 지원하기 때문에 객체 지향 프로그래밍에서 핵심이 되는 객체 (사물) 을 표현하는 것이
 * 가능하다. (즉, 클래스를 통해 객체가 지니는 속성과 행위를 표현하는 것이 가능하다.)
 * 
 * C# 클래스 선언 방법
 * - class + 클래스 이름 + 클래스 멤버 (변수, 메서드 등등...)
 * 
 * Ex)
 * class CCharacter {
 *     public int m_nLV = 0;
 *     public int m_nHP = 0;
 *     public int m_nATK = 0;
 *     
 *     public void ShowInfo() {
 *         // Do Something
 *     }
 * }
 */
namespace E01 {
	/** 캐릭터 */
	public class CE06Character {
		public int m_nLV = 0;
		public int m_nHP = 0;
		public int m_nATK = 0;

		/** 정보를 출력한다 */
		public void ShowInfo() {
			Debug.Log($"레벨 : {m_nLV}");
			Debug.Log($"체력 : {m_nHP}");
			Debug.Log($"공격력 : {m_nATK}");
		}
	}

	/** Example 7 */
	public partial class CE01Example_07 : CE01SceneManager {
		#region 프로퍼티
		public override string SceneName => KE01Define.G_SCENE_N_EXAMPLE_07;
		#endregion // 프로퍼티

		#region 함수
		/** 초기화 */
		public override void Awake() {
			base.Awake();

			var oCharacter = new CE06Character();
			oCharacter.m_nLV = 1;
			oCharacter.m_nHP = 10;
			oCharacter.m_nATK = 15;

			Debug.Log("=====> 캐릭터 <=====");
			oCharacter.ShowInfo();
		}
		#endregion // 함수
	}
}
