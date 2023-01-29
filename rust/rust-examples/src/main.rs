mod constants;
mod files;

fn main() {
    println!("Hello, world!");
    let content = rust::run(rust::TEN);
    println!("{:#?}", content);

    let file_content = files::read_file(constants::TEN).unwrap();
    println!("{}", file_content);
    rust::run_all();
    files::run_all();
}
