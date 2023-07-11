document.querySelector('#add-item').addEventListener('click', function () {
    const item_count = document.getElementById('item_count').value;
    var item;
    switch (item_count) {
      case "1":
        item = document.getElementById('item2');
        item.style.display = "block";
        document.getElementById('item_count').value = "2";
        break;
      case "2":
        item = document.getElementById('item3');
        item.style.display = "block";
        document.getElementById('item_count').value = "3";
        break;
      case "3":
        item = document.getElementById('item4');
        item.style.display = "block";
        document.getElementById('item_count').value = "4";
        break;
      case "4":
        item = document.getElementById("item5");
        item.style.display = "block";
        document.getElementById('item_count').value = "5";
        break;
      case "5":
        alert("これ以上3Dイメージを追加出来ません");
        break;
    };

  })

  document.querySelector('#delete-item').addEventListener('click', function () {
    const item_count = document.getElementById('item_count').value;
    var item;
    var cssText;
    switch (item_count) {
      case "1":
        alert("これ以上削除できません");
        break;
      case "2":
        item = document.getElementById('item2');
        cssText = item.style.cssText + ';display:none !important;';
        item.style.cssText = cssText;

        document.getElementById('item_count').value = "1";
        break;
      case "3":
        item = document.getElementById('item3');
        cssText = item.style.cssText + ';display:none !important;';
        item.style.cssText = cssText;

        document.getElementById('item_count').value = "2";
        break;
      case "4":
        item = document.getElementById("item4");
        cssText = item.style.cssText + ';display:none !important;';
        item.style.cssText = cssText;

        document.getElementById('item_count').value = "3";
        break;
      case "5":
        item = document.getElementById("item5");
        cssText = item.style.cssText + ';display:none !important;';
        item.style.cssText = cssText;
        document.getElementById('item_count').value = "4";
        break;
    };

  })

   // item1
   document.querySelector('#item1_positionX').addEventListener('change', function () {
    var p = document.getElementById('item1_positionX').value;
    document.getElementById('item1_posiX_value').textContent = p;
  })

  document.querySelector('#item1_positionY').addEventListener('change', function () {
    var p = document.getElementById('item1_positionY').value;
    document.getElementById('item1_posiY_value').textContent = p;
  })

  document.querySelector('#item1_positionZ').addEventListener('change', function () {
    var p = document.getElementById('item1_positionZ').value;
    document.getElementById('item1_posiZ_value').textContent = p;
  })

  document.querySelector('#item1_scale').addEventListener('change', function () {
    var p = document.getElementById('item1_scale').value;
    document.getElementById('item1_scale_value').textContent = p;
  })

  // item2

  document.querySelector('#item2_positionX').addEventListener('change', function () {
    var p = document.getElementById('item2_positionX').value;
    document.getElementById('item2_posiX_value').textContent = p;
  })

  document.querySelector('#item2_positionY').addEventListener('change', function () {
    var p = document.getElementById('item2_positionY').value;
    document.getElementById('item2_posiY_value').textContent = p;
  })

  document.querySelector('#item2_positionZ').addEventListener('change', function () {
    var p = document.getElementById('item2_positionZ').value;
    document.getElementById('item2_posiZ_value').textContent = p;
  })

  document.querySelector('#item2_scale').addEventListener('change', function () {
    var p = document.getElementById('item2_scale').value;
    document.getElementById('item2_scale_value').textContent = p;
  })

  // item3

  document.querySelector('#item3_positionX').addEventListener('change', function () {
    var p = document.getElementById('item3_positionX').value;
    document.getElementById('item3_posiX_value').textContent = p;
  })

  document.querySelector('#item3_positionY').addEventListener('change', function () {
    var p = document.getElementById('item3_positionY').value;
    document.getElementById('item3_posiY_value').textContent = p;
  })

  document.querySelector('#item3_positionZ').addEventListener('change', function () {
    var p = document.getElementById('item3_positionZ').value;
    document.getElementById('item3_posiZ_value').textContent = p;
  })

  document.querySelector('#item3_scale').addEventListener('change', function () {
    var p = document.getElementById('item3_scale').value;
    document.getElementById('item3_scale_value').textContent = p;
  })

  // item4

  document.querySelector('#item4_positionX').addEventListener('change', function () {
    var p = document.getElementById('item4_positionX').value;
    document.getElementById('item4_posiX_value').textContent = p;
  })

  document.querySelector('#item4_positionY').addEventListener('change', function () {
    var p = document.getElementById('item4_positionY').value;
    document.getElementById('item4_posiY_value').textContent = p;
  })

  document.querySelector('#item4_positionZ').addEventListener('change', function () {
    var p = document.getElementById('item4_positionZ').value;
    document.getElementById('item4_posiZ_value').textContent = p;
  })

  document.querySelector('#item4_scale').addEventListener('change', function () {
    var p = document.getElementById('item4_scale').value;
    document.getElementById('item4_scale_value').textContent = p;
  })

   // item5

   document.querySelector('#item5_positionX').addEventListener('change', function () {
    var p = document.getElementById('item5_positionX').value;
    document.getElementById('item5_posiX_value').textContent = p;
  })

  document.querySelector('#item5_positionY').addEventListener('change', function () {
    var p = document.getElementById('item5_positionY').value;
    document.getElementById('item5_posiY_value').textContent = p;
  })

  document.querySelector('#item5_positionZ').addEventListener('change', function () {
    var p = document.getElementById('item5_positionZ').value;
    document.getElementById('item5_posiZ_value').textContent = p;
  })

  document.querySelector('#item5_scale').addEventListener('change', function () {
    var p = document.getElementById('item5_scale').value;
    document.getElementById('item5_scale_value').textContent = p;
  })



