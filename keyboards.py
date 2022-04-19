from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_ukraine = InlineKeyboardButton('Ukraine', callback_data='ukraine')
inline_netherlands = InlineKeyboardButton('Netherlands', callback_data='netherlands')
inline_norway = InlineKeyboardButton('Norway', callback_data='norway')
inline_greece = InlineKeyboardButton('Greece', callback_data='greece')
inline_albania = InlineKeyboardButton('Albania', callback_data='albania')
inline_armenia = InlineKeyboardButton('Armenia', callback_data='armenia')
inline_moldova = InlineKeyboardButton('Moldova', callback_data='moldova')
inline_portugal = InlineKeyboardButton('Portugal', callback_data='portugal')
inline_swiss = InlineKeyboardButton('Switzerland', callback_data='swiss')
inline_austria = InlineKeyboardButton('Austria', callback_data='austria')
inline_lithuania = InlineKeyboardButton('Lithuania', callback_data='lithuania')
inline_latvia = InlineKeyboardButton('Latvia', callback_data='latvia')
inline_croatia = InlineKeyboardButton('Croatia', callback_data='croatia')
inline_iceland = InlineKeyboardButton('Iceland', callback_data='iceland')
inline_slovenia = InlineKeyboardButton('Slovenia', callback_data='slovenia')
inline_denmark = InlineKeyboardButton('Denmark', callback_data='denmark')
inline_bulgaria = InlineKeyboardButton('Bulgaria', callback_data='bulgaria')
inline_kb = InlineKeyboardMarkup(row_width=4)
inline_kb.row(inline_greece, inline_norway, inline_netherlands, inline_ukraine)
inline_kb.row(inline_moldova, inline_portugal, inline_armenia, inline_albania)
inline_kb.row(inline_latvia, inline_lithuania, inline_swiss, inline_austria)
inline_kb.row(inline_bulgaria, inline_denmark, inline_iceland, inline_croatia, inline_slovenia)

inline_sweden = InlineKeyboardButton('Sweden', callback_data='sweden')
inline_poland = InlineKeyboardButton('Poland', callback_data='poland')
inline_estonia = InlineKeyboardButton('Estonia', callback_data='estonia')
inline_finland = InlineKeyboardButton('Finland', callback_data='finland')
inline_azerbaijan = InlineKeyboardButton('Azerbaijan', callback_data='azerbaijan')
inline_australia = InlineKeyboardButton('Australia', callback_data='australia')
inline_serbia = InlineKeyboardButton('Serbia', callback_data='serbia')
inline_belgium = InlineKeyboardButton('Belgium', callback_data='belgium')
inline_czech = InlineKeyboardButton('Czech Rep.', callback_data='czech')
inline_cyprus = InlineKeyboardButton('Cyprus', callback_data='cyprus')
inline_malta = InlineKeyboardButton('Malta', callback_data='malta')
inline_romania = InlineKeyboardButton('Romania', callback_data='romania')
inline_san = InlineKeyboardButton('San Marino', callback_data='marino')
inline_montenegro = InlineKeyboardButton('Montenegro', callback_data='montenegro')
inline_israel = InlineKeyboardButton('Israel', callback_data='israel')
inline_macedonia = InlineKeyboardButton('N. Macedonia', callback_data='macedonia')
inline_ireland = InlineKeyboardButton('Ireland', callback_data='ireland')
inline_georgia = InlineKeyboardButton('Georgia', callback_data='georgia')
inline_kb_2 = InlineKeyboardMarkup(row_width=4)
inline_kb_2.row(inline_ireland, inline_israel, inline_san, inline_macedonia)
inline_kb_2.row(inline_malta, inline_montenegro, inline_czech, inline_cyprus)
inline_kb_2.row(inline_serbia, inline_sweden, inline_poland, inline_romania, inline_belgium)
inline_kb_2.row(inline_finland, inline_australia, inline_azerbaijan, inline_estonia, inline_georgia)

inline_italy = InlineKeyboardButton('Italy', callback_data='italy')
inline_uk = InlineKeyboardButton('The UK', callback_data='uk')
inline_spain = InlineKeyboardButton('Spain', callback_data='spain')
inline_france = InlineKeyboardButton('France', callback_data='france')
inline_germany = InlineKeyboardButton('Germany', callback_data='germany')
inline_kb_3 = InlineKeyboardMarkup(row_width=5)
inline_kb_3.row(inline_france, inline_uk, inline_spain, inline_germany, inline_italy)

inline_vote_norway = InlineKeyboardButton('Norway', callback_data='Norway')
inline_vote_ukraine = InlineKeyboardButton('Ukraine', callback_data='Ukraine')
inline_vote_netherlands = InlineKeyboardButton('Netherlands', callback_data='Netherlands')
inline_vote_greece = InlineKeyboardButton('Greece', callback_data='Greece')
inline_vote_albania = InlineKeyboardButton('Albania', callback_data='Albania')
inline_vote_armenia = InlineKeyboardButton('Armenia', callback_data='Armenia')
inline_vote_moldova = InlineKeyboardButton('Moldova', callback_data='Moldova')
inline_vote_portugal = InlineKeyboardButton('Portugal', callback_data='Portugal')
inline_vote_swiss = InlineKeyboardButton('Switzerland', callback_data='Swiss')
inline_vote_austria = InlineKeyboardButton('Austria', callback_data='Austria')
inline_vote_lithuania = InlineKeyboardButton('Lithuania', callback_data='Lithuania')
inline_vote_latvia = InlineKeyboardButton('Latvia', callback_data='Latvia')
inline_vote_croatia = InlineKeyboardButton('Croatia', callback_data='Croatia')
inline_vote_iceland = InlineKeyboardButton('Iceland', callback_data='Iceland')
inline_vote_slovenia = InlineKeyboardButton('Slovenia', callback_data='Slovenia')
inline_vote_denmark = InlineKeyboardButton('Denmark', callback_data='Denmark')
inline_vote_bulgaria = InlineKeyboardButton('Bulgaria', callback_data='Bulgaria')
inline_vote_sweden = InlineKeyboardButton('Sweden', callback_data='Sweden')
inline_vote_poland = InlineKeyboardButton('Poland', callback_data='Poland')
inline_vote_estonia = InlineKeyboardButton('Estonia', callback_data='Estonia')
inline_vote_finland = InlineKeyboardButton('Finland', callback_data='Finland')
inline_vote_azerbaijan = InlineKeyboardButton('Azerbaijan', callback_data='Azerbaijan')
inline_vote_australia = InlineKeyboardButton('Australia', callback_data='Australia')
inline_vote_serbia = InlineKeyboardButton('Serbia', callback_data='Serbia')
inline_vote_belgium = InlineKeyboardButton('Belgium', callback_data='Belgium')
inline_vote_czech = InlineKeyboardButton('Czech Rep.', callback_data='Czech')
inline_vote_cyprus = InlineKeyboardButton('Cyprus', callback_data='Cyprus')
inline_vote_malta = InlineKeyboardButton('Malta', callback_data='Malta')
inline_vote_romania = InlineKeyboardButton('Romania', callback_data='Romania')
inline_vote_san = InlineKeyboardButton('San Marino', callback_data='Marino')
inline_vote_montenegro = InlineKeyboardButton('Montenegro', callback_data='Montenegro')
inline_vote_israel = InlineKeyboardButton('Israel', callback_data='Israel')
inline_vote_macedonia = InlineKeyboardButton('N. Macedonia', callback_data='Macedonia')
inline_vote_ireland = InlineKeyboardButton('Ireland', callback_data='Ireland')
inline_vote_georgia = InlineKeyboardButton('Georgia', callback_data='Georgia')
inline_vote_italy = InlineKeyboardButton('Italy', callback_data='Italy')
inline_vote_uk = InlineKeyboardButton('The UK', callback_data='UK')
inline_vote_spain = InlineKeyboardButton('Spain', callback_data='Spain')
inline_vote_france = InlineKeyboardButton('France', callback_data='France')
inline_vote_germany = InlineKeyboardButton('Germany', callback_data='Germany')
inline_voting = InlineKeyboardMarkup(row_width=5)
inline_voting.row(inline_vote_norway, inline_vote_uk, inline_vote_romania, inline_vote_germany,
                  inline_vote_france)
inline_voting.row(inline_vote_macedonia, inline_vote_georgia, inline_vote_spain, inline_vote_san, inline_vote_denmark)
inline_voting.row(inline_vote_italy, inline_vote_montenegro, inline_vote_azerbaijan, inline_vote_armenia,
                  inline_vote_czech)
inline_voting.row(inline_vote_serbia, inline_vote_iceland, inline_vote_ireland, inline_vote_israel, inline_vote_malta)
inline_voting.row(inline_vote_cyprus, inline_vote_belgium, inline_vote_australia, inline_vote_austria,
                  inline_vote_croatia)
inline_voting.row(inline_vote_poland, inline_vote_sweden, inline_vote_estonia, inline_vote_finland, inline_vote_latvia)
inline_voting.row(inline_vote_bulgaria, inline_vote_lithuania, inline_vote_swiss, inline_vote_slovenia,
                  inline_vote_greece)
inline_voting.row(inline_vote_moldova, inline_vote_albania, inline_vote_portugal, inline_vote_ukraine,
                  inline_vote_netherlands)
