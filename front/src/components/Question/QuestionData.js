export function data() {
  return [
    {
      id: "ef-4c43-d68",
      name: "Vue.js의 라이프 사이클이 아닌 것은?",
      country: "객관식",
      난이도: 3,
      slogan: 1,
      keywords: ["Vue.js", "Frontend", "Javascript", "면접"],
      answers: ["computed", "created", "mount", "beforemount"],
      correct_ans: "mount",
    },
    {
      id: "4a-4a93-cfe",
      name: "다음 발표자는?",
      country: "객관식",
      난이도: 5,
      slogan: 1,
      keywords: ["면접"],
    },
    {
      id: "8a-4809-144",
      name: "과연 나는 디자인 감각이 있는가?",
      country: "OX퀴즈",
      난이도: 1,
      slogan: 0,
      keywords: ["면접", "디자인"],
    },
    {
      id: "8a-4809-145",
      name: "언제쯤 잘 할 수 있을까?",
      country: "주관식",
      난이도: 1,
      slogan: 2,
      keywords: ["면접", "Frontend"],
      answers: ["김태우", "김기은", "정지수", "정영훈", "정영길"],
      correct_ans: "김태우",
    },
    {
      id: "8a-4809-147",
      name: "태우형은 이런거 금방 하겠지?",
      country: "단답형",
      난이도: 5,
      slogan: 3,
      keywords: ["Frontend", "디자인"],
      answers: [],
      correct_ans: "당연한 소리",
    },
    {
      id: "8a-4809-148",
      name: "코린이는 울어요",
      country: "녹음",
      난이도: 4,
      slogan: 4,
      keywords: ["Code"],
      answers: [],
      correct_ans: "녹음은 어케합니까?",
    },
  ];
}
export function data2() {
  return [
    {
      problems: {
        p_question: "Vue.js의 라이프 사이클이 아닌 것은?",
        p_code: "code string",
        pc_id: "Web",
        pt_id: 2,
        pd_id: 5,
      },
      answers: ["computed", "created", "mount", "beforemount"],
      correct_ans: "mount",
    },
    {
      problems: {
        p_question: "다음 발표자는?",
        p_code: "code string",
        pc_id: "기타",
        pt_id: 2,
        pd_id: 5,
      },
      answers: ["김태우", "김기은", "정지수", "정영훈", "정영길"],
      correct_ans: "김태우",
    },
  ];
}
