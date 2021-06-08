$(document).ready(() => {
  $("#sidebar").animate({ width: 0 }, 400, () => {
    $("#sidebar").hide();
  });

  $("#open-sidebar").click(() => {
    $("#sidebar").show("fast", () => {
      $("#sidebar").animate({ width: 200 });
    });
  });

  $("#close-sidebar").click(() => {
    $("#sidebar").animate({ width: 0 }, 400, () => {
      $("#sidebar").hide();
    });
  });
});
