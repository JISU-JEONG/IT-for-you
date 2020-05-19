const inputs = document.getElementsByTagName("input"); //응답
const questions = document.getElementsByTagName("section"); //질문
const selectedQuestion = document.getElementsByClassName("current"); //현재 질문 버튼

const button = document.getElementsByClassName("nextButton"); // 다음 질문 버튼
for (let i = 0; i < button.length; i++) {
  button[i].onclick = function() {
    nextQuestion(i);
  };
}

function nextQuestion(i) {
  if (questions[i] === selectedQuestion[0]) {
    questions[i].className = "";
    questions[i + 1].className = "current";
  }
}

// 정답 체크
const submit = document.getElementById("submitAnswers");
submit.onclick = function() {
  answersArray();
};

function answersArray() {
  let answers = [];
  let correctAnswers = ["mount", "a"]; //정답 배열
  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].checked) {
      answers.push(inputs[i].value);
    }
  }

  let correctCount = 0;
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === correctAnswers[i]) {
      correctCount++;
    }
  }
  alert(
    "You got " +
      correctCount +
      " out of " +
      answers.length +
      " answers correct!"
  );
}

if (document.createElement("svg").getAttributeNS) {
  // 응답
  const radiobxsFill = Array.prototype.slice.call(
    document.querySelectorAll('#questionsList input[type="radio"]')
  );

  const pathDefs = {
    fill: [
      "M15.833,24.334c2.179-0.443,4.766-3.995,6.545-5.359 c1.76-1.35,4.144-3.732,6.256-4.339c-3.983,3.844-6.504,9.556-10.047,13.827c-2.325,2.802-5.387,6.153-6.068,9.866 c2.081-0.474,4.484-2.502,6.425-3.488c5.708-2.897,11.316-6.804,16.608-10.418c4.812-3.287,11.13-7.53,13.935-12.905 c-0.759,3.059-3.364,6.421-4.943,9.203c-2.728,4.806-6.064,8.417-9.781,12.446c-6.895,7.477-15.107,14.109-20.779,22.608 c3.515-0.784,7.103-2.996,10.263-4.628c6.455-3.335,12.235-8.381,17.684-13.15c5.495-4.81,10.848-9.68,15.866-14.988 c1.905-2.016,4.178-4.42,5.556-6.838c0.051,1.256-0.604,2.542-1.03,3.672c-1.424,3.767-3.011,7.432-4.723,11.076 c-2.772,5.904-6.312,11.342-9.921,16.763c-3.167,4.757-7.082,8.94-10.854,13.205c-2.456,2.777-4.876,5.977-7.627,8.448 c9.341-7.52,18.965-14.629,27.924-22.656c4.995-4.474,9.557-9.075,13.586-14.446c1.443-1.924,2.427-4.939,3.74-6.56 c-0.446,3.322-2.183,6.878-3.312,10.032c-2.261,6.309-5.352,12.53-8.418,18.482c-3.46,6.719-8.134,12.698-11.954,19.203 c-0.725,1.234-1.833,2.451-2.265,3.77c2.347-0.48,4.812-3.199,7.028-4.286c4.144-2.033,7.787-4.938,11.184-8.072 c3.142-2.9,5.344-6.758,7.925-10.141c1.483-1.944,3.306-4.056,4.341-6.283c0.041,1.102-0.507,2.345-0.876,3.388 c-1.456,4.114-3.369,8.184-5.059,12.212c-1.503,3.583-3.421,7.001-5.277,10.411c-0.967,1.775-2.471,3.528-3.287,5.298 c2.49-1.163,5.229-3.906,7.212-5.828c2.094-2.028,5.027-4.716,6.33-7.335c-0.256,1.47-2.07,3.577-3.02,4.809",
    ],
  };

  let animDefs = {
    fill: { speed: 0.8, easing: "ease-in-out" },
  };

  const createSVGEl = () => {
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttributeNS(null, "viewBox", "0 0 100 100");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    return svg;
  };

  radiobxsFill.forEach(function(el, i) {
    // 각 응답들 안에 SVG 추가
    let svg = createSVGEl();
    el.parentNode.appendChild(svg);
    el.addEventListener("change", function() {
      resetRadio(el); // 그려진 SVG 지우기
      draw(el); // SVG 그리기
    });
  });

  const resetRadio = (el) => {
    // 번호들을 확인해서 svg가 그려진것이 있으면 remove
    Array.prototype.slice
      .call(
        document.querySelectorAll(
          'input[type="radio"][name="' + el.getAttribute("name") + '"]'
        )
      )
      .forEach(function(el) {
        var path = el.parentNode.querySelector("svg > path");
        if (path) {
          path.parentNode.removeChild(path);
        }
      });
  };

  const draw = (el) => {
    let paths = [];
    const pathDef = pathDefs.fill;
    const animDef = animDefs.fill;
    const svg = el.parentNode.querySelector("svg");

    paths.push(document.createElementNS("http://www.w3.org/2000/svg", "path"));
    for (var i = 0, len = paths.length; i < len; ++i) {
      let path = paths[i];
      svg.appendChild(path);

      path.setAttributeNS(null, "d", pathDef[i]);
      var length = path.getTotalLength();
      path.style.strokeDasharray = length + " " + length;
      path.style.strokeDashoffset = Math.floor(length) - 1;
      path.setAttributeNS(null, "fill", "white");
      path.getBoundingClientRect();
      path.style.transition = path.style.WebkitTransition = path.style.MozTransition =
        "stroke-dashoffset " +
        animDef.speed +
        "s " +
        animDef.easing +
        " " +
        i * animDef.speed +
        "s";
      path.style.strokeDashoffset = "0";
    }
  };
}
