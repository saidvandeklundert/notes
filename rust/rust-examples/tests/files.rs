use rust;
#[test]
fn true_ok() {
    assert_eq!(true, true);
    let result = rust::files::read_file("./tests/files/ten.txt").unwrap();

    assert!(result.contains("ten"))
}
