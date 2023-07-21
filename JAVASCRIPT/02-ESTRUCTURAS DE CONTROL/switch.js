let v = 'F',print = '';

switch (v) {
    case 'a':
    case 'A':
    case 'e':
    case 'E':
    case 'i':
    case 'I':
    case 'o':
    case 'O':
    case 'u':
    case 'U':
        print = `${v} es VOCAL`;
        break;

    default:
        print = `${v} NO ES VOCAL`
}

console.log(print);
