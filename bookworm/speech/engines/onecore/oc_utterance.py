# coding: utf-8

from System.Globalization import CultureInfo, CultureNotFoundException
from bookworm.speech.enumerations import SpeechElementKind
from bookworm.speech.utterance import SpeechElement, SpeechStyle
from bookworm.logger import logger
from ..sapi.sp_utterance import SapiSpeechUtterance

try:
    from OcSpeechElements import PromptBuilder as OcPromptBuilder
except:
    OcPromptBuilder = None


log = logger.getChild(__name__)


class OcSpeechUtterance(SapiSpeechUtterance):

    def __init__(self, synth):
        super().__init__()
        self.synth = synth
        self._speech_sequence = []
        self._heal_funcs = []

    def process_speech_element(self, elm_kind, content):
        if elm_kind is SpeechElementKind.start_paragraph:
            super().process_speech_element(elm_kind, content)
            self._heal_funcs.append((self.prompt.EndParagraph, ()))
        elif elm_kind is SpeechElementKind.start_style:
            super().process_speech_element(elm_kind, content)
            self._heal_funcs.append((self.end_style, (content,)))
        else:
            super().process_speech_element(elm_kind, content)

    def add_bookmark(self, bookmark):
        """Append application specific data."""
        self._speech_sequence.append(self._pop_prompt_content())
        self._speech_sequence.append(SpeechElement(SpeechElementKind.bookmark, bookmark))

    def _pop_prompt_content(self):
        for func, args in self._heal_funcs:
            func(*args)
        self._heal_funcs.clear()
        voice = self.synth().voice
        voice_utterance = SapiSpeechUtterance()
        with voice_utterance.set_style(SpeechStyle(voice=voice, rate=self.synth().rate)):
            voice_utterance.append_utterance(self)
        voice_utterance.prompt.Culture = CultureInfo.GetCultureInfoByIetfLanguageTag(voice.language)
        rv = voice_utterance.prompt.ToXml()
        if not self.prompt.IsEmpty:
            self.prompt.ClearContent()
        return SpeechElement(SpeechElementKind.ssml, rv)

    def to_oc_prompt(self):
        oc_prompt = OcPromptBuilder()
        if not self.prompt.IsEmpty:
            self._speech_sequence.append(self._pop_prompt_content())
        for element in self._speech_sequence:
            if element.kind is SpeechElementKind.ssml:
                oc_prompt.AddSsml(element.content)
            elif element.kind is SpeechElementKind.bookmark:
                oc_prompt.AddBookmark(element.content)
        return oc_prompt